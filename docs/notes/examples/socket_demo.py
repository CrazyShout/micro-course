"""Python 3 version of the Chapter 2 uppercase example, loopback only.
Manual: --transport udp|tcp --role server|client --port 12000
Self-test: --self-test (records actual local execution, including TCP framing).
"""
from pathlib import Path
import socket,argparse,threading,json,datetime
HOST='127.0.0.1';LIMIT=8192
def line(sock):
    data=bytearray()
    while b'\n' not in data:
        part=sock.recv(64)
        if not part:raise EOFError('Connection ended before the newline-delimited message was complete.')
        data.extend(part)
        if len(data)>LIMIT:raise ValueError('Teaching message exceeds the size limit.')
    return bytes(data).split(b'\n',1)[0]
def serve(transport,port,ready=None):
    kind=socket.SOCK_DGRAM if transport=='udp' else socket.SOCK_STREAM
    with socket.socket(socket.AF_INET,kind) as server:
        server.settimeout(15);server.bind((HOST,port))
        actual=server.getsockname()[1]
        if transport=='tcp':server.listen(1)
        if ready is not None:ready['port']=actual;ready['event'].set()
        else:print(f'{transport.upper()} server ready on {HOST}:{actual}; one request only.',flush=True)
        if transport=='udp':
            data,address=server.recvfrom(LIMIT+1)
            if len(data)>LIMIT:raise ValueError('Datagram too large for this example.')
            reply=data.decode('utf-8').upper().encode('utf-8')
            server.sendto(reply,address)
        else:
            connection,address=server.accept()
            with connection:
                connection.settimeout(5);request=line(connection)
                connection.sendall(request.decode('utf-8').upper().encode('utf-8')+b'\n')
def client(transport,port,message):
    if '\n' in message:raise ValueError('Use a single line in this teaching example.')
    data=message.encode('utf-8')
    if len(data)>LIMIT-1:raise ValueError('Message is too long.')
    kind=socket.SOCK_DGRAM if transport=='udp' else socket.SOCK_STREAM
    with socket.socket(socket.AF_INET,kind) as sock:
        sock.settimeout(5)
        if transport=='udp':
            sock.sendto(data,(HOST,port));reply,address=sock.recvfrom(LIMIT)
            assert address[0]==HOST and address[1]==port
        else:
            sock.connect((HOST,port));sock.sendall(data+b'\n');reply=line(sock)
    return reply.decode('utf-8')
def self_test():
    rows=[]
    for transport,message in [('udp','hello network'),('tcp','course practice'),('tcp','long text '*300)]:
        ready={'event':threading.Event()};errors=[]
        def run():
            try:serve(transport,0,ready)
            except Exception as e:errors.append(repr(e));ready['event'].set()
        thread=threading.Thread(target=run,daemon=True);thread.start()
        if not ready['event'].wait(5) or errors:raise RuntimeError(f'Server startup failed: {errors}')
        reply=client(transport,ready['port'],message);thread.join(5)
        assert not thread.is_alive() and not errors and reply==message.upper()
        rows.append({'transport':transport,'request_bytes':len(message.encode()),'reply_bytes':len(reply.encode()),'expected_uppercase':True})
    out=Path(__file__).resolve().parents[1]/'observations/socket-self-test.json';out.parent.mkdir(exist_ok=True)
    report={'observed_at':datetime.datetime.now().astimezone().isoformat(),'address':HOST,'tests':rows,'scope':'Actual loopback socket I/O; not an Internet network measurement.'}
    out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--self-test',action='store_true');p.add_argument('--transport',choices=['udp','tcp'],default='udp');p.add_argument('--role',choices=['client','server'],default='client');p.add_argument('--port',type=int,default=12000);p.add_argument('--message',default='hello network');a=p.parse_args()
    if a.self_test:self_test()
    elif a.role=='server':serve(a.transport,a.port)
    else:print(client(a.transport,a.port,a.message))
