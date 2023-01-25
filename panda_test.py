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

        #self.cube = self.loader.loadModel("models/misc/rgbCube")
        self.sphere = self.loader.loadModel("models/misc/sphere")
        self.sphere.reparentTo(self.render)
        self.sphere.setScale(1, 1, 1)
        self.sphere.setPos(0, 20, 0)

        self.cube = self.loader.loadModel("models/misc/rgbCube")
        self.cube.reparentTo(self.render)
        self.cube.setScale(1, 1, 1)
        self.cube.setPos(5, 20, 0)

app = MyApp()
app.run()
