from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, 'pages/index.html')

def processor(request):
    return render(request, 'pages/processor.html')

def graphics(request):
    return render(request, 'pages/graphics.html')

def storage(request):
    return render(request, 'pages/storage.html')

def motherboard(request):
    return render(request, 'pages/motherboard.html')

def ram(request):
    return render(request, 'pages/ram.html')

def references(request):
    return render(request, 'pages/references.html')

def graphics2(request):
    return render(request, 'pages/graphics2.html')

def processor2(request):
    return render(request, 'pages/processor2.html')

def storage2(request):
    return render(request, 'pages/storage2.html')

def Create_User(request):

    if request.method == 'POST':
        user = User.objects.create(username = request.POST['username'],
            email = request.POST['email'],
            career = request.POST['career'],)
        user.save()

        return redirect(f'/createbuild/{user.id}/')

    else:
        return render(request, 'user_form.html')

def Create_Build(request, user_id):

    user =  User.objects.get(id = user_id)

    processor = Processor_dropdown.objects.all()
    motherboard = Motherboard_dropdown.objects.all()
    storage = Storage_dropdown.objects.all()
    ram = Ram_dropdown.objects.all()
    graphics = Graphics_dropdown.objects.all()
    powersupply = Powersupply_dropdown.objects.all()
    chassis = Chassis_dropdown.objects.all()
    fan = Fan_dropdown.objects.all()


    if request.method == 'POST':
        price = request.POST['budget_']

        parts = Parts.objects.create(processor = request.POST['1model-processesor'],
            motherboard = request.POST['motherboard'],
            powersupply = request.POST['powersupply'],
            ram = request.POST['rams'],
            storage = request.POST['size-storage'],
            fan = request.POST['fan'],
            graphicscard = request.POST['graphics-card'],
            chassis = request.POST['pc_case'],)

        parts.save()


        build = Build.objects.create(builder_info = user,
            computer_parts = parts,
            price = price)

        build.save()

        return redirect(f'/buildlist/{user.id}/') 

    else:
        return render(request, 'find-your-pc.html', {'user':user,
            'processor':processor,
            'motherboard': motherboard,
            'storage':storage,
            'ram':ram,
            'graphics':graphics,
            'powersupply':powersupply,
            'chassis':chassis,
            'fan':fan})

def BuildList(request, user_id):
    user = User.objects.get(id = user_id)
    build = Build.objects.filter(builder_info = user_id)
    users = User.objects.get(pk = user_id)
    return render(request, 'user_build_list.html', {'Build':build, 'User':users})

def Delete(request, build_id):
    build = Build.objects.get(id=build_id)
    builder_id = Build.builder_info
    build.delete()
    return redirect(f'/buildlist/{build.builder_info.id}/')

def Edit(request, build_id):
    processor = Processor_dropdown.objects.all()
    motherboard = Motherboard_dropdown.objects.all()
    storage = Storage_dropdown.objects.all()
    ram = Ram_dropdown.objects.all()
    graphics = Graphics_dropdown.objects.all()
    powersupply = Powersupply_dropdown.objects.all()
    chassis = Chassis_dropdown.objects.all()
    fan = Fan_dropdown.objects.all()

    build = Build.objects.get(id=build_id)
    return render(request, 'form_pc_parts_update.html', {'build':build,
        'processor':processor,
        'motherboard': motherboard,
        'storage':storage,
        'ram':ram,
        'graphics':graphics,
        'powersupply':powersupply,
        'chassis':chassis,
        'fan':fan})


def Update(request, build_id):
    build = Build.objects.get(id=build_id)
    
    # if request.method == "POST":

    #     build.price = request.POST['budget_']
    #     build.computer_parts.processor = request.POST['1model-processesor']
    #     build.computer_parts.motherboard = request.POST['motherboard']
    #     build.computer_parts.powersupply = request.POST['powersupply']
    #     build.computer_parts.ram = request.POST['rams']
    #     build.computer_parts.storage = request.POST['size-storage']
    #     build.computer_parts.fan = request.POST['fan']
    #     build.computer_parts.graphicscard = request.POST['graphics-card']
    #     build.computer_parts.chassis = request.POST['pc_case']
    #     build.save()

    return redirect(f'/buildlist/{build.builder_info.id}/')




#old
    # def find_pc_view(request):
    #     processor_dropdown = Processor_dropdown.objects.all()
    #     return render(request, 'find-your-pc.html', {'processor_d': processor_dropdown})

    # def add_build_page_view(request, user_id):
    #     user = User.objects.get(id = user_id)
    #     if request.method == 'POST':
    #         price = request.POST['budget_']

    #         parts = Parts.objects.create(processor = request.POST['1model-processesor'],
    #             motherboard = request.POST['motherboard'],
    #             powersupply = request.POST['powersupply'],
    #             ram = request.POST['rams'],
    #             storage = request.POST['size-storage'],
    #             fan = request.POST['fan'],
    #             graphicscard = request.POST['graphics-card'],
    #             chassis = request.POST['pc_case'],)

    #         upgrade = Upgrade.objects.create()
    #         addons = PeripheralDevices.objects.create()

    #         Build.objects.create(builder_info = user,
    #             computer_parts = parts,
    #             addons = addons,
    #             upgrade = upgrade,
    #             price = price)

    #         return redirect(f'/myApp/buildlist/{user.id}/')

    #     else:
    #         return render(request, 'add_new_build.html', {'user':user})

    # def UserBuildList_view(request, user_id):
    #     user = User.objects.get(id = user_id)

    #     if request.method == 'POST':
    #         return redirect(f'/myApp/addnewbuild/{user.id}/')
    #     else:
    #         build = Build.objects.filter(builder_info = user_id)
    #         users = User.objects.get(pk = user_id)
    #         return render(request, 'user_build_list.html', {'Build':build, 'User':users})


    # def Create_List(request):
    #     user = User.objects.create(username = request.POST['user'])
    #     price = request.POST['budget_']

    #     parts = Parts.objects.create(processor = request.POST['1model-processesor'],
    #         motherboard = request.POST['motherboard'],
    #         powersupply = request.POST['powersupply'],
    #         ram = request.POST['rams'],
    #         storage = request.POST['size-storage'],
    #         fan = request.POST['fan'],
    #         graphicscard = request.POST['graphics-card'],
    #         chassis = request.POST['pc_case'],)

    #     upgrade = Upgrade.objects.create()
    #     addons = PeripheralDevices.objects.create()
    #     Build.objects.create(builder_info = user,
    #         computer_parts = parts,
    #         addons = addons,
    #         upgrade = upgrade,
    #         price = price)

    #     return redirect(f'/myApp/buildlist/{user.id}/')


    # def Add_New_Build_To_List(request, user_id):
    #     user = User.objects.get(id = user_id)

    #     price = request.POST['budget_']

    #     parts = Parts.objects.create(processor = request.POST['1model-processesor'],
    #         motherboard = request.POST['motherboard'],
    #         powersupply = request.POST['powersupply'],
    #         ram = request.POST['rams'],
    #         storage = request.POST['size-storage'],
    #         fan = request.POST['fan'],
    #         graphicscard = request.POST['graphics-card'],
    #         chassis = request.POST['pc_case'],)

    #     upgrade = Upgrade.objects.create()
    #     addons = PeripheralDevices.objects.create()

    #     Build.objects.create(builder_info = user,
    #         computer_parts = parts,
    #         addons = addons,
    #         upgrade = upgrade,
    #         price = price)

    #     return redirect(f'/myApp/buildlist/{user.id}/')