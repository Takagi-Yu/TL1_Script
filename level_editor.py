import bpy

# ブレンダーに登録するアドオン情報
bl_info = {
    "name": "レベルエディタ",
    "author": "yuu takagi",
    "version": (1,0),
    "blender": (3,3,1),
    "location": "",
    "description": "レベルエディタ",
    "warning": "",
    "support":"TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

# メニュー項目描画
def draw_menu_manual(self,context):
    #self : 呼び出し元のクラスインスタンス。C++でいうとthisポインタ
    #context : カーソルを合わせた時のポップアップのカスタマイズなどに使用

    #トップバーの「エディターメニュー」に項目(オペレータ)を追加
    self.layout.operator("wm.url_open_preset",text="Manual",icon='HELP')

# アドオン有効化時コールバック
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_editor_menus.append(TOPBER_MT_my_menu.submenu)
    print("レベルエディタが有効化されました。")

# アドオン無効化時コールバック
def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(draw_menu_manual)
    print("レベルエディタが無効化されました。")
    
class TOPBER_MT_my_menu(bpy.types.Menu):
    bl_idname = "TOPBAR_MT_my_menu"
    bl_label = "MyMenu"
    bl_description = "拡張メニュー by " + bl_info["author"]

    def draw(self, context):
        self.layout.operator("wm.url_open_preset",text="Manual",icon='HELP')

    def submenu(self,context):
        self.layout.menu(TOPBER_MT_my_menu.bl_idname)

clases =(TOPBER_MT_my_menu,)