@namespace
class SpriteKind:
    _stone = SpriteKind.create()
    _box = SpriteKind.create()
    _dog = SpriteKind.create()
裝飾石頭: Sprite = None
寶箱: Sprite = None
寵物: Sprite = None
tiles.set_tilemap(tilemap("""
    層級1
"""))
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
mySprite.set_position(361, 24)
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
for value in tiles.get_tiles_by_type(assets.tile("""
    myTile8
""")):
    寵物 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . 3 3 3 . . 
                    . . . . . . . . 3 3 3 . 3 . . . 
                    . . . . . 3 3 3 . . . 3 . . . . 
                    . . . 3 3 . . . . . 3 . . . . . 
                    . . . . . . . . 3 3 . . . . . . 
                    . . . . . . . 3 . . . . . . . . 
                    . . . . . . 3 . . . . . . . . . 
                    . . . . . . . 3 . . . . . . . . 
                    . . . . . . . . 3 3 3 . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind._dog)
    tiles.place_on_tile(寵物, value)
for value2 in tiles.get_tiles_by_type(assets.tile("""
    myTile7
""")):
    寶箱 = sprites.create(assets.tile("""
        myTile1
    """), SpriteKind._box)
    tiles.place_on_tile(寶箱, value2)
for value3 in tiles.get_tiles_by_type(assets.tile("""
    myTile9
""")):
    裝飾石頭 = sprites.create(assets.tile("""
        rock0
    """), SpriteKind._stone)
    tiles.place_on_tile(裝飾石頭, value3)