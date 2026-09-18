/* Small article experiments. Fixed example/exercise data and study state stay untouched. */
(() => {
  'use strict';
  let sequence = 0;
  const fixed = (n, digits = 4) => (Math.abs(n) < 0.5 * 10 ** -digits ? 0 : n).toFixed(digits);

  function gaussian(host) {
    const id = `gaussian-article-${++sequence}`;
    host.innerHTML = `
      <p><strong>换一个条件，机器会改口吗？ / Change one assumption</strong></p>
      <p>固定样本 x = (2, 0)，均值 μ<sub>A</sub> = (0, 0)、μ<sub>B</sub> = (4, 0)，Σ<sub>A</sub> = diag(4, 1)，Σ<sub>B</sub> = diag(v, 1)。只改变 B 的第一维方差 v 或 A 的先验。独立教学演示，不改变正文题目的条件。</p>
      <div class="demo-controls">
        <label for="${id}-variance">B 的方差 v / Variance
          <select id="${id}-variance" data-variance>
            <option value="1" selected>1</option><option value="4">4</option><option value="16">16</option>
          </select>
        </label>
        <label for="${id}-prior">A 的先验 P(A) / Prior
          <select id="${id}-prior" data-prior>
            <option value="0.2">0.2</option><option value="0.5" selected>0.5</option><option value="0.8">0.8</option>
          </select>
        </label>
        <button type="button" data-reset>恢复默认 / Reset</button>
      </div>
      <div class="demo-result" data-result aria-live="polite" aria-atomic="true"></div>
      <p>这里特征无量纲，ln 是自然对数；q = (x − μ)ᵀΣ⁻¹(x − μ)。分数省略两类共有的 −ln(2π)，取值可为负；后验才是归一化后的概率。This dimensionless teaching model uses natural logs and omits the shared constant.</p>`;
    const variance = host.querySelector('[data-variance]');
    const prior = host.querySelector('[data-prior]');
    const result = host.querySelector('[data-result]');
    const update = () => {
      const v = [1, 4, 16].includes(Number(variance.value)) ? Number(variance.value) : 1;
      const p = [0.2, 0.5, 0.8].includes(Number(prior.value)) ? Number(prior.value) : 0.5;
      const rows = [
        {name: 'A', logPrior: Math.log(p), width: -0.5 * Math.log(4), distance: -0.5 * 4 / 4},
        {name: 'B', logPrior: Math.log(1 - p), width: -0.5 * Math.log(v), distance: -0.5 * 4 / v},
      ];
      rows.forEach(row => { row.score = row.logPrior + row.width + row.distance; });
      const max = Math.max(...rows.map(row => row.score));
      const weights = rows.map(row => Math.exp(row.score - max));
      const denominator = weights.reduce((a, b) => a + b, 0);
      rows.forEach((row, index) => { row.posterior = weights[index] / denominator; });
      const tie = Math.abs(rows[0].score - rows[1].score) < 1e-10;
      const prediction = tie ? '两类并列 / Tie' : `${rows[0].score > rows[1].score ? 'A' : 'B'}`;
      result.innerHTML = `
        <p>当前 P(A) = ${p.toFixed(1)}，P(B) = ${(1 - p).toFixed(1)}，v = ${v}。<strong>预测 / Prediction：${prediction}</strong></p>
        <p class="article-table-hint">← 窄屏可横向滑动表格 / Swipe table →</p><div class="table-scroll" tabindex="0"><table aria-label="Gaussian class score contributions and posterior probabilities">
          <thead><tr><th scope="col">类 / Class</th><th scope="col">先验 ln P(C)</th><th scope="col">宽度 −½ ln |Σ|</th><th scope="col">距离 −½ q</th><th scope="col">总分 s</th><th scope="col">后验 / Posterior</th></tr></thead>
          <tbody>${rows.map(row => `<tr><th scope="row">${row.name}</th><td>${fixed(row.logPrior)}</td><td>${fixed(row.width)}</td><td>${fixed(row.distance)}</td><td>${fixed(row.score)}</td><td>${fixed(row.posterior)} (${fixed(row.posterior * 100, 1)}%)</td></tr>`).join('')}</tbody>
        </table></div>
        <p>${tie ? '这组条件让两类的分数完全相同。模型不能仅凭这些条件偏向其中一类。 / Equal scores give no preference.' : '看清哪一项改变了判断：先验改变类的常见程度；方差同时改变距离惩罚和分布宽度，不能只看其中一项。 / Variance changes both distance and spread terms.'}</p>`;
    };
    variance.addEventListener('change', update);
    prior.addEventListener('change', update);
    host.querySelector('[data-reset]').addEventListener('click', () => {
      variance.value = '1';
      prior.value = '0.5';
      update();
    });
    update();
  }

  function cafe(host) {
    const id = `cafe-article-${++sequence}`;
    const capacity = 600;
    const demandPerUser = 300;
    const p = 0.2;
    const states = Array.from({length: 8}, (_, n) => {
      const bits = n.toString(2).padStart(3, '0');
      const count = [...bits].reduce((sum, bit) => sum + Number(bit), 0);
      return {bits, count, probability: p ** count * (1 - p) ** (3 - count)};
    }).sort((a, b) => a.count - b.count || a.bits.localeCompare(b.bits));
    host.innerHTML = `
      <p><strong>三位顾客，现在谁在上传？ / Who is active?</strong></p>
      <p>每人活跃时需求 300 kbps，共享容量 600 kbps。勾选表示“此刻活跃”，不是随机抽样。独立教学演示，不改变正文练习。</p>
      <div class="cafe-users">
        ${['A', 'B', 'C'].map((name, index) => `<label for="${id}-${name}"><input id="${id}-${name}" type="checkbox" data-user="${index}" ${index < 2 ? 'checked' : ''}> 顾客 ${name} / User ${name}</label>`).join('')}
      </div>
      <div class="demo-controls"><button type="button" data-reset>恢复默认 / Reset</button></div>
      <div class="demo-result" data-result aria-live="polite" aria-atomic="true"></div>
      <p>概率表假设每人独立且以相同概率 p = 0.2 活跃，1 为活跃，0 为空闲。它计算需求超过容量的概率，不直接给出排队时长或丢包概率。独立性在大家同时开会或同步上传时可能不成立。The table assumes independent users; demand overflow is not a queue-delay or packet-loss probability.</p>`;
    const users = [...host.querySelectorAll('[data-user]')];
    const result = host.querySelector('[data-result]');
    const update = () => {
      const chosen = users.map(user => user.checked ? '1' : '0').join('');
      const count = users.filter(user => user.checked).length;
      const demand = count * demandPerUser;
      const over = demand > capacity;
      const exactTwo = states.filter(state => state.count === 2).reduce((sum, state) => sum + state.probability, 0);
      const overflow = states.filter(state => state.count * demandPerUser > capacity).reduce((sum, state) => sum + state.probability, 0);
      result.innerHTML = `
        <p>当前状态 / State：<strong>${chosen}</strong>，K = ${count}。需求 / Demand：<strong>${demand} kbps</strong>；容量 / Capacity：${capacity} kbps。</p>
        <div class="capacity-track${over ? ' over' : ''}" role="img" aria-label="Demand ${demand} kbps; capacity ${capacity} kbps"><span style="width:${Math.min(demand / capacity, 1) * 100}%"></span></div>
        <p><strong>${over ? `超过容量 ${demand - capacity} kbps / Demand exceeds capacity` : demand === capacity ? '刚好等于容量，不算超额 / Exactly at capacity, not over' : '需求未超过容量 / Demand is within capacity'}</strong>。${over ? '如何排队、是否丢包还要看持续时间、缓存与调度。' : '这里仅比较这个状态下的需求；不能据此断言真实网络一定没有排队。'}</p>
        <p class="article-table-hint">← 窄屏可横向滑动表格 / Swipe table →</p><div class="table-scroll" tabindex="0"><table aria-label="Eight activity states for three independent users">
          <thead><tr><th scope="col">ABC 状态 / State</th><th scope="col">活跃数 K</th><th scope="col">概率 / Probability</th><th scope="col">需求 / Demand</th><th scope="col">超过 600？ / Over?</th></tr></thead>
          <tbody>${states.map(state => `<tr class="${state.count * demandPerUser > capacity ? 'over-capacity ' : ''}${state.bits === chosen ? 'selected-state' : ''}"><th scope="row">${state.bits}${state.bits === chosen ? ' ← 当前 / selected' : ''}</th><td>${state.count}</td><td>${fixed(state.probability, 3)}</td><td>${state.count * demandPerUser} kbps</td><td>${state.count * demandPerUser > capacity ? '是 / Yes' : '否 / No'}</td></tr>`).join('')}</tbody>
        </table></div>
        <p>P(K = 2) = 3 × 0.2² × 0.8 = <strong>${fixed(exactTwo, 3)}</strong>；P(K &gt; 2) = 0.2³ = <strong>${fixed(overflow, 3)}</strong>。勾选只选中一行，不改变模型概率。Selecting a row does not change these probabilities.</p>`;
    };
    users.forEach(user => user.addEventListener('change', update));
    host.querySelector('[data-reset]').addEventListener('click', () => {
      users.forEach((user, index) => { user.checked = index < 2; });
      update();
    });
    update();
  }

  window.mountArticleDemo = (host, type) => {
    if (type === 'gaussian-score') gaussian(host);
    else if (type === 'cafe-capacity') cafe(host);
    else throw new Error(`Unknown article demo: ${type}`);
  };
})();
