bl_info = {
    "name": "Happy New Year Addon Hüseyin Oğuz Kahveci",
    "author": "YHüseyin Oğuz Kahveci",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > UI",
    "description": "Adds animation about Happy New Year Celebration",
    "warning": "",
    "support": "COMMUNITY",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"
}

import bpy
import random
import math
import csv

#sahnede öncelikle herşeyi temizlememiz gerekiyor, bu yüzden delete fonksiyonu oluşturuldu
def delete_all():

    if(len(bpy.data.objects) != 0):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)

#sahnede isimleri farklı bir yerden almamak için, terminale direkt göndermek adına csv dosyalarını okuma fonksiyonu oluşturuldu
def read_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

#sahnede değişken olarak text oluşturuldu, bu değişkenlerden ilki tebrik mesajı
def add_text(text):
    first_frame = 1
    second_frame = 25
    bpy.ops.object.text_add(location=(0, -6, 0))
    text_object = bpy.context.object
    text_object.data.body = text
    text_object.data.align_x = 'CENTER'
    text_object.data.align_y = 'CENTER'
    text_object.data.extrude = 0.1
    text_object.data.bevel_depth = 0.02
    text_object.scale = (0.01, 0.01, 0.01)
    text_object.keyframe_insert(data_path="scale", frame=first_frame)
    text_object.location[1] = -17.50
    text_object.location[2] = 2.02
    text_object.rotation_euler[0] = 1.5708
    text_object.data.materials.append(bpy.data.materials.new(name="NeonRed"))
    text_object.active_material.diffuse_color = (1, 0, 0 ,1)
    text_object.active_material.specular_intensity = 1.0
    text_object.scale = (0.12, 0.12, 0.12)
    text_object.keyframe_insert(data_path="scale", frame=second_frame)
    
#sahnede değişken olarak text oluşturuldu, bu değişkenlerden ikincisi kimi tebrik ettiğimiz
def add_text2(text2):
    first_frame = 1
    second_frame = 25
    bpy.ops.object.text_add(location=(0, -7, 0))
    text_object2 = bpy.context.object
    text_object2.data.body = text2
    text_object2.data.align_x = 'CENTER'
    text_object2.data.align_y = 'CENTER'
    text_object2.data.extrude = 0.1
    text_object2.data.bevel_depth = 0.02
    text_object2.scale = (0.01, 0.01, 0.01)
    text_object2.keyframe_insert(data_path="scale", frame=first_frame)
    text_object2.location[1] = -17.50
    text_object2.location[2] = 2.2
    text_object2.rotation_euler[0] = 1.5708
    text_object2.data.materials.append(bpy.data.materials.new(name="Neonclr2"))
    text_object2.active_material.diffuse_color = (0, 1, 0 ,1)
    text_object2.active_material.specular_intensity = 1.0
    text_object2.scale = (0.1, 0.1, 0.1)
    text_object2.keyframe_insert(data_path="scale", frame=second_frame)

#sahnede değişken olarak text oluşturuldu, bu değişkenlerden ikincisi kimin tebrik ettiği
def add_text3(text3):
    first_frame = 1
    second_frame = 25
    bpy.ops.object.text_add(location=(0, -8, 0))
    text_object3 = bpy.context.object
    text_object3.data.body = text3
    text_object3.data.align_x = 'CENTER'
    text_object3.data.align_y = 'CENTER'
    text_object3.data.extrude = 0.1
    text_object3.data.bevel_depth = 0.02
    text_object3.scale = (0.01, 0.01, 0.01)
    text_object3.keyframe_insert(data_path="scale", frame=first_frame)
    text_object3.location[0] = 0.4
    text_object3.location[1] = -17.50
    text_object3.location[2] = 1.82
    text_object3.rotation_euler[0] = 1.5708
    text_object3.data.materials.append(bpy.data.materials.new(name="Neonclr3"))
    text_object3.active_material.diffuse_color = (0, 0, 1 ,1)
    text_object3.active_material.specular_intensity = 1.0
    text_object3.scale = (0.05, 0.05, 0.05)
    text_object3.keyframe_insert(data_path="scale", frame=second_frame)

#sahnede havaii fişek efekti verebilmek için sphere oluşturuldu
#havaii fişekler bir noktadan patlayarak yukarı doğru hareket ettirildi
def create_animated_spheres(num_spheres_per_group):
    for i in range(8):
        for j in range(num_spheres_per_group):   
            bpy.ops.mesh.primitive_uv_sphere_add(radius=0.09, location=(0, 6.5, -0.2))
            sphere = bpy.context.object
            sphere.active_material = bpy.data.materials.new(name="SphereMaterial")
            sphere.active_material.diffuse_color = (random.random(), random.random(), random.random() ,1.0)
        for j, sphere in enumerate(bpy.data.objects):
            if sphere.type == 'MESH':
                sphere.keyframe_insert(data_path='location', frame=i*25)
                sphere.location.x += random.uniform(-10, 10)
                sphere.location.y += random.uniform(-5, 5)
                sphere.location.z += random.uniform(7, 11)
                sphere.keyframe_insert(data_path='location', frame=(i+1)*25) 

#sahnede ağaç oluşturulmak için silindir ve koni yapıları kullanıldı
#ağaç yapıları düzenlenip sahneye istenilen kadar eklenmesi için randomiz eklendi   
def tree_maker(treemake):
    for i in range(treemake):
        x = random.uniform(-8, 8)
        y = random.uniform(0, 5)
        z = 0.5 
        bpy.ops.mesh.primitive_cylinder_add(radius=0.1, depth=1, location=(x, y, z))
        trunk = bpy.context.active_object
        trunk.name = "TreeTrunk_"+str(i)
        mat = bpy.data.materials.new("TreeTrunkMaterial")
        mat.diffuse_color = (0.65, 0.35, 0.25, 1.0)
        trunk.data.materials.append(mat)
        z += 1
        bpy.ops.mesh.primitive_cone_add(radius1=0.5, radius2=0, depth=1, location=(x, y, z))
        tree_top = bpy.context.active_object
        tree_top.name = "TreeTop_"+str(i)
        mat = bpy.data.materials.new("TreeTopMaterial")
        mat.diffuse_color = (0, 0.5, 0, 1.0)
        tree_top.data.materials.append(mat)
        for i in range(1, 5):
            bpy.ops.mesh.primitive_cone_add(radius1=0.5-(i*0.1), radius2=0, depth=1, location=(x, y, 1.5+(i*0.5)))
            top = bpy.context.active_object
            top.name = "TreeTop_"+str(i)
            top.data.materials.append(mat)

#sahnenin sağ tarafında bulunan okun içine(view_3d>ui, item, tool, view diye ilerleyen kısma) en alta addonun paneli yerleştirildi
#panele sahne içinde öncelikle her şeyi silen alt panel eklendi
#alt seçeneğe kar taneleri eklendi, kar taneleri matematikteki altıgen dendrit formülü kullanılarak yapıldı
#bir alt seçeneğe eğer isim listesi isteniyorsa terminale isimleri yazdırabilecek bicsv file reader konuldu ve path için seçenek verildi
#bir alt panelde mesajın ne olacağı, kime gideceği ve kimden gideceği seçeneklerini yazabileceğimiz belirtildi
#bir alt panele topların (havaii fişeklerin) sayısını belirleyip ekleyebileceğimiz alt panel verildi, render ve görsel durumuna göre ayarlama getirildi
#bir alt panelde sahne elemanları(ışık, kamera vb.) elemanlar eklendi
#bir alt panele de sahenmize ağaç paneli eklendi, top sayısı gibi ağaçların sayısı da görsel ve render durumuna göre ayarlanabilir hale geldi
class MyTextPanel(bpy.types.Panel):
    bl_label = "Happy New Year Animation"
    bl_idname = "OBJECT_PT_my_animation_addon"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    #operatörlerin panelleri eklendi
    def draw(self, context):
        layout = self.layout
        layout.operator("object.delete_all", text="Delete Everything on Scene")
        layout.operator("object.snowflake_generator", text="Generate Snowflake")
        row = layout.row()
        row.prop(context.scene, "my_addon_csv_filepath")
        row = layout.row()
        row.operator("my_addon.read_csv", text="Read CSV and see names in terminal")
        row = layout.row()
        row.prop(context.scene, "text_value", text="Message")
        row.operator("object.add_text", text="Add Text", icon='FILE_REFRESH')
        row = layout.row()
        row.prop(context.scene, "text_value2", text="to who")
        row.operator("object.add_text2", text="Add Text", icon='FILE_REFRESH')
        row = layout.row()
        row.prop(context.scene, "text_value3", text="from who")
        row.operator("object.add_text3", text="Add Text", icon='FILE_REFRESH')
        row = layout.row()
        row.prop(context.scene, "num_spheres", text="Number of Spheres")
        row.operator("object.create_animated_spheres", text="Create Animated Spheres", icon='FILE_REFRESH')
        layout.operator("object.scene_generator", text="Generate Scene")
        row = layout.row()
        row.prop(context.scene, "num_trees", text="Number of Trees")
        row.operator("object.tree_maker", text="Add Trees", icon='FILE_REFRESH')
        row = layout.row()

#sahnedeki objeleri silen class yapısı oluşturuldu        
class DeletingGenerator(bpy.types.Operator):
    bl_idname = "object.delete_all"
    bl_label = "Deleting Generator"

    def execute(self, context):
        if(len(bpy.data.objects) != 0):
            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.delete(use_global=False)
        return {'FINISHED'}

#sahnedeki isme aktarılacak olan csv dosyasındaki isimleri okuyan class yapısı oluşturuldu
class MyAddonReadCSVOperator(bpy.types.Operator):
    bl_idname = "my_addon.read_csv"
    bl_label = "Read CSV and see names in terminal"

    def execute(self, context):
        filepath = context.scene.my_addon_csv_filepath
        read_csv(filepath)
        return {'FINISHED'}

#sahnedeki kar tanelerini oluşturan class yapısı oluşturuldu
class SnowflakeGenerator(bpy.types.Operator):
    bl_idname = "object.snowflake_generator"
    bl_label = "Snowflake Generator"

    def execute(self, context):
        num_branches = 5
        angle = 2 * math.pi / num_branches
        length = 1
        radius = 0.1

        for i in range(num_branches):
            bpy.ops.mesh.primitive_cylinder_add(radius=radius/2, depth=length, location=(0, 0, length/2))
            cylinder = bpy.context.object

            cylinder.rotation_euler[1] = i * angle
            cylinder.rotation_euler[2] = angle/2

            cylinder.scale[0] = (num_branches - i) / num_branches
            cylinder.scale[1] = (num_branches - i) / num_branches

        mat = bpy.data.materials.new("DendriteMaterial")
        mat.diffuse_color = (0.5, 0.5, 0.5, 1)
        bpy.context.object.data.materials.append(mat)

        for obj in bpy.context.scene.objects:
            if obj.type == 'MESH':
                obj.select_set(True)
            bpy.ops.object.join()

        bpy.context.object.scale[0] = 0.04
        bpy.context.object.scale[1] = 0.01
        bpy.context.object.scale[2] = 0.16

        #ardından sahnedeki kar tanesi yapısı bir objeye emitter olarak atanıp emitter özellikleri belirlendi
        for obj in bpy.context.selected_objects:
            obj.name = "emitterobject"
            obj.data.name = "emitterobject"
            
        bpy.ops.mesh.primitive_ico_sphere_add(enter_editmode=False, align='WORLD', location=(0, -8, 8), scale=(0.1, 0.1, 0.1))
        bpy.ops.object.particle_system_add()
        bpy.data.particles["ParticleSettings"].render_type = 'OBJECT'
        bpy.data.particles["ParticleSettings"].instance_object = bpy.data.objects["emitterobject"]
        bpy.data.particles["ParticleSettings"].lifetime = 200
        bpy.data.particles["ParticleSettings"].particle_size = 1
        bpy.data.particles["ParticleSettings"].timestep = 0.003
        bpy.data.particles["ParticleSettings"].use_rotations = True
        bpy.data.particles["ParticleSettings"].rotation_factor_random = 0.5
        bpy.data.particles["ParticleSettings"].phase_factor = 0.25
        bpy.data.particles["ParticleSettings"].phase_factor_random = 1.5
        bpy.data.particles["ParticleSettings"].use_dynamic_rotation = True
        bpy.data.particles["ParticleSettings"].angular_velocity_factor = 3
        bpy.data.particles["ParticleSettings"].normal_factor = 20
        bpy.data.particles["ParticleSettings"].object_align_factor[2] = -14
        bpy.data.particles["ParticleSettings"].count = 9000
        return {'FINISHED'}

#text operatörün ilki göndermek istediğimiz mesajı içeriyor, bu mesajı yazan class yapısı oluşturuldu
class AddTextOperator(bpy.types.Operator):
    bl_idname = "object.add_text"
    bl_label = "Add Text"

    def execute(self, context):
        add_text(context.scene.text_value)
        return {'FINISHED'}

#text operatörün ikincisi göndermek istediğimiz kişiyi içeriyor, bu mesajı yazan class yapısı oluşturuldu
class AddTextOperator2(bpy.types.Operator):
    bl_idname = "object.add_text2"
    bl_label = "Add Text"

    def execute(self, context):
        add_text2(context.scene.text_value2)
        return {'FINISHED'}

#text operatörün üçüncüsü göndermek isteyen kişiyi içeriyor, bu mesajı yazan class yapısı oluşturuldu
class AddTextOperator3(bpy.types.Operator):
    bl_idname = "object.add_text3"
    bl_label = "Add Text"

    def execute(self, context):
        add_text3(context.scene.text_value3)
        return {'FINISHED'}

#havaii fişekleri oluşturan kürelerin class yapısı oluşturuldu
class CreateAnimatedSpheresOperator(bpy.types.Operator):
    bl_idname = "object.create_animated_spheres"
    bl_label = "Create Animated Spheres"

    def execute(self, context):
        create_animated_spheres(context.scene.num_spheres)
        return {'FINISHED'}

#sahnenin ışıklandırılması kamerası frame sayısı arka planı oluşturacak plane yapıları ve sahnenin shading tipi bu classta oluşturuldu
class ScenePropsOperator(bpy.types.Operator):
    bl_idname = "object.scene_generator"
    bl_label = "Scene Generator"

    def execute(self, context):
        bpy.context.scene.frame_start = 1
        bpy.context.scene.frame_end = 200
        bpy.ops.object.light_add(type='POINT', radius=1, location=(-2, -17.75, 2.3))
        light_object = bpy.context.object
        light_object.data.energy = 15
        light_object.hide_viewport = False
        bpy.ops.object.light_add(type='POINT', radius=1, location=(-1, -17.75, 2.3))
        light_object = bpy.context.object
        light_object.data.energy = 15
        light_object.hide_viewport = False
        bpy.ops.object.light_add(type='POINT', radius=1, location=(0, -17.75, 2.3))
        light_object = bpy.context.object
        light_object.data.energy = 15
        light_object.hide_viewport = False
        bpy.ops.object.light_add(type='POINT', radius=1, location=(1, -17.75, 2.3))
        light_object = bpy.context.object
        light_object.data.energy = 15
        light_object.hide_viewport = False
        bpy.ops.object.light_add(type='POINT', radius=1, location=(2, -17.75, 2.3))
        light_object = bpy.context.object
        light_object.data.energy = 15
        light_object.hide_viewport = False
        bpy.ops.object.light_add(type='SUN', radius=1, align='WORLD', location=(0, -14, -1), scale=(1, 1, 1))
        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, -19, 2), rotation=(1.570796, 0, 0), scale=(1, 1, 1))
        bpy.context.object.data.lens = 41
        bpy.ops.mesh.primitive_plane_add(size=200, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.ops.mesh.primitive_plane_add(size=200, enter_editmode=False, align='WORLD', location=(0, 30, -5), scale=(1, 1, 1))
        bpy.context.object.rotation_euler[0] = 0.453789
        bpy.context.space_data.shading.type = 'RENDERED'
        return {'FINISHED'}

#ağaçları oluşturan class yapısı oluşturuldu
class TreeMakerOperator(bpy.types.Operator):
    bl_idname = "object.tree_maker"
    bl_label = "Create Trees"

    def execute(self, context):
        tree_maker(context.scene.num_trees)
        return {'FINISHED'}

#sahnedeki classları atayan reigster fonksiyonu tanımlandı
def register():
    bpy.types.Scene.my_addon_csv_filepath = bpy.props.StringProperty(
        name="CSV File Path",
        description="Path to CSV file to read",
        default="",
        subtype='FILE_PATH'
    )
    bpy.types.Scene.text_value = bpy.props.StringProperty(name="Message", default="Happy New Year")
    bpy.types.Scene.text_value2 = bpy.props.StringProperty(name="to who", default="Ahmet")
    bpy.types.Scene.text_value3 = bpy.props.StringProperty(name="from who", default="Mehmet")
    bpy.types.Scene.num_spheres = bpy.props.IntProperty(name="Number of Spheres", default=100, min=0)
    bpy.types.Scene.num_trees = bpy.props.IntProperty(name="Number of Trees", default=10, min=0)
    bpy.utils.register_class(MyTextPanel)
    bpy.utils.register_class(MyAddonReadCSVOperator)
    bpy.utils.register_class(SnowflakeGenerator)
    bpy.utils.register_class(DeletingGenerator)
    bpy.utils.register_class(AddTextOperator)
    bpy.utils.register_class(AddTextOperator2)
    bpy.utils.register_class(AddTextOperator3)
    bpy.utils.register_class(CreateAnimatedSpheresOperator)
    bpy.utils.register_class(ScenePropsOperator)
    bpy.utils.register_class(TreeMakerOperator)

#sahnedeki classları bellekten kaldıran unregister fonksiyonu tanımlandı
def unregister():
    del bpy.types.Scene.text_value
    del bpy.types.Scene.text_value2
    del bpy.types.Scene.text_value3
    del bpy.types.Scene.num_spheres
    del bpy.types.Scene.num_trees
    bpy.utils.unregister_class(MyTextPanel)
    bpy.utils.unregister_class(MyAddonReadCSVOperator)
    bpy.utils.unregister_class(SnowflakeGenerator)
    bpy.utils.unregister_class(DeletingGenerator)
    bpy.utils.unregister_class(AddTextOperator)
    bpy.utils.unregister_class(AddTextOperator2)
    bpy.utils.unregister_class(AddTextOperator3)
    bpy.utils.unregister_class(CreateAnimatedSpheresOperator)
    bpy.utils.unregister_class(ScenePropsOperator)
    bpy.utils.unregister_class(TreeMakerOperator)
 

if __name__ == "__main__":
    register()