'''ゲームエンジン「Panda3D」のテスト'''
from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    '''テスト用のクラス'''
    def __init__(self):
        ShowBase.__init__(self)

        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(1, 1, 1)
        self.scene.setPos(0, 0, 0)

app = MyApp()
app.run()
