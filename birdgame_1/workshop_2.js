// エンジンの更新ごと(毎フレーム)に実行される処理
Events.on(engine, 'afterUpdate', () => {
  // 発射中かつ鳥が発射点を越えたら、ゴムの制約を解除して自由に飛ばす
  if (isFiring && tori.position.x > bane.x + 10) {
    gattai.bodyB = null; // 接続を解除
    gattai.render.visible = false;
    isFiring = false;
  }
});

// 世界(world)に全ての物体(地面、鳥、ゴム、マウス制約、箱の束)を追加
Composite.add(world, [jimen, tori, gattai, mouseConstraint, ...hako]);

// 描画とエンジンの実行を開始
Render.run(render);
const runner = Runner.create();
Runner.run(runner, engine);

// キャンバスの見た目をPico.cssのスタイルに合わせて調整
render.canvas.style.width = '100%';
render.canvas.style.height = 'auto';
render.canvas.style.borderRadius = '8px';
