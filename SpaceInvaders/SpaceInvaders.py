import cocos

class MainLayer(cocos.layer.Layer):
    def __init__(self):
        super(MainLayer, self).__init__()
        self.player = cocos.sprite.Sprite("ball.png")
        self.player.position = (320, 240)
        self.add(self.player)

if __name__ == "__main__":
    cocos.director.director.init(caption="Hello, Cocos")
    layer = MainLayer()
    scene = cocos.scene.Scene(layer)
    cocos.director.director.run(scene)
