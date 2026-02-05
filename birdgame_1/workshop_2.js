// 描画とエンジンの実行を開始
Render.run(render);
const runner = Runner.create();
Runner.run(runner, engine);

// キャンバスの見た目をPico.cssのスタイルに合わせて調整
render.canvas.style.width = '100%';
render.canvas.style.height = 'auto';
render.canvas.style.borderRadius = '8px';
