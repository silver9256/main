from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from myApp.models import *


class HomepageTest(TestCase):
	def test_mainpage_equal_template(self):
	    response = self.client.get('/')
	    self.assertTemplateUsed(response, 'find-your-pc.html')

class ORMTEST(TestCase):
	def test_saving_retriv(self):
		user = User()
		user.username = 'Silver Ganadores'
		user.email = 'silver@gmail.com'
		user.career = 'teacher'
		user.save()

		parts = Parts()
		parts.processor = 'Intel Core i5-3450'
		parts.motherboard = 'Gigabyte GA-H61M-DS2'
		parts.storage = 'Kingspec -- 120gb'
		parts.ram = '4GB Kingston HyperX Fury DDR4 2400Mhz'
		parts.graphicscard = 'Colorful GeForce GT730K -- 2gb'
		parts.powerSupply = 'RAKK 400 watts'
		parts.chassis = 'Rakk Marug -- MicroATX'
		parts.fan = 'Allan 12V Fan -- 80mm'
		parts.save()

		upgrade = Upgrade()
		upgrade.save()

		peripheraldevices = PeripheralDevices()
		peripheraldevices.save()

		build = Build()
		build.builder_info = user
		build.computer_parts = parts
		build.purpose = 'Gaming'
		build.price = 10000
		build.addons = peripheraldevices
		build.upgrade = upgrade
		build.save()

		build2 = Build()
		build2.builder_info = user
		build2.computer_parts = parts
		build2.purpose = 'Office'
		build2.price = 10000
		build2.addons = peripheraldevices
		build2.upgrade = upgrade
		build2.save()

		savedBuild = Build.objects.first()

		self.assertEqual(build, savedBuild)

		allBuilds = Build.objects.all()

		self.assertEqual(allBuilds.count(), 2)

		self.assertEqual(allBuilds[0].purpose, 'Gaming')
		self.assertEqual(allBuilds[1].purpose, 'Office')

		self.assertEqual(allBuilds[0].builder_info.username, 'Silver Ganadores')
		self.assertEqual(allBuilds[1].builder_info.username, 'Silver Ganadores')

class CreateListTest(TestCase):

	def test_save_POST_request(self):
		response = self.client.post('/myApp/createlist/',
			{'user': 'Silver Ganadores',
			'budget_': 10000,
			'1model-processesor': 'Intel Core i5-3450',
			'motherboard': 'Gigabyte GA-H61M-DS2',
			'powersupply': 'RAKK 400 watts',
			'rams': '4GB Kingston HyperX Fury DDR4 2400Mhz',
			'size-storage': 'Kingspec -- 120gb',
			'fan': 'Allan 12V Fan -- 80mm',
			'graphics-card': 'Colorful GeForce GT730K -- 2gb',
			'pc_case': 'Rakk Marug -- MicroATX',})


		self.assertEqual(PeripheralDevices.objects.count(), 1)
		#print('pdevices is okay')
		self.assertEqual(Upgrade.objects.count(), 1)
		#print('upgrade is okay')
		self.assertEqual(User.objects.count(), 1)
		self.assertEqual(Parts.objects.count(), 1)
		self.assertEqual(Build.objects.count(), 1)

		user = User.objects.first()
		chosen_parts = Parts.objects.first()
		self.assertEqual(user.username, 'Silver Ganadores')

		self.assertEqual(chosen_parts.processor, 'Intel Core i5-3450')
		self.assertEqual(chosen_parts.motherboard, 'Gigabyte GA-H61M-DS2')
		self.assertEqual(chosen_parts.powersupply, 'RAKK 400 watts')
		self.assertEqual(chosen_parts.ram, '4GB Kingston HyperX Fury DDR4 2400Mhz')
		self.assertEqual(chosen_parts.storage, 'Kingspec -- 120gb')
		self.assertEqual(chosen_parts.fan, 'Allan 12V Fan -- 80mm')
		self.assertEqual(chosen_parts.graphicscard, 'Colorful GeForce GT730K -- 2gb')
		self.assertEqual(chosen_parts.chassis, 'Rakk Marug -- MicroATX')

	def test_POST_redirect(self):
		response = self.client.post('/myApp/createlist/',
			{'user': 'Silver Ganadores',
			'budget_': 10000,
			'1model-processesor': 'Intel Core i5-3450',
			'motherboard': 'Gigabyte GA-H61M-DS2',
			'powersupply': 'RAKK 400 watts',
			'rams': '4GB Kingston HyperX Fury DDR4 2400Mhz',
			'size-storage': 'Kingspec -- 120gb',
			'fan': 'Allan 12V Fan -- 80mm',
			'graphics-card': 'Colorful GeForce GT730K -- 2gb',
			'pc_case': 'Rakk Marug -- MicroATX',})
		user = User.objects.first()
		self.assertRedirects(response, f'/myApp/buildlist/{user.id}/')

class ViewTest(TestCase):
	def test_displays_each_reg(self):

		user = User.objects.create(username = 'Silver')
		build1 = Parts.objects.create(processor = 'Intel Core i5-3450',
	    	motherboard = 'Gigabyte GA-H61M-DS2',
	    	powersupply = 'RAKK 400 watts',
	    	ram = '4GB Kingston HyperX Fury DDR4 2400Mhz',
	        storage = 'Kingspec -- 120gb',
	        fan = 'Allan 12V Fan -- 80mm',
	        graphicscard = 'Colorful GeForce GT730K -- 2gb',
	        chassis = 'Rakk Marug -- MicroATX',)

		build2 = Parts.objects.create(processor = 'AMD',
	    	motherboard = 'Gigabyte GA-H61M-DS2',
	    	powersupply = 'RAKK 400 watts',
	    	ram = '4GB Kingston HyperX Fury DDR4 2400Mhz',
	        storage = 'Kingspec -- 120gb',
	        fan = 'Allan 12V Fan -- 80mm',
	        graphicscard = 'Colorful GeForce GT730K -- 2gb',
	        chassis = 'Rakk Marug -- MicroATX',)


		upgrade = Upgrade.objects.create()
		perip = PeripheralDevices.objects.create()
		
		Build.objects.create(builder_info = user,
			computer_parts = build1,
			addons = perip,
			upgrade = upgrade)

		Build.objects.create(builder_info = user,
			computer_parts = build2,
			addons = perip,
			upgrade = upgrade)
		

		self.assertEqual(Build.objects.count(), 2)
		#print('2 build objects')
		response = self.client.get(f'/myApp/buildlist/{user.id}/')
		self.assertContains(response, 'Intel Core i5-3450')
		self.assertContains(response, 'AMD')
		#print('may AMD')

	def test_listview_uses_listpage(self):
		user = User.objects.create()
		response = self.client.get(f'/myApp/buildlist/{user.id}/')
		self.assertTemplateUsed(response, 'user_build_list.html')

class Add_New_Build_To_List(TestCase):
	def test_add_POST_request_to_exisiting_list(self):
		user1 = User.objects.create(username = 'Silver')
		user2 = User.objects.create(username = 'Adore')

		response = self.client.post(f'/myApp/addlist/{user1.id}/',
			{'budget_': 10000,
			'1model-processesor': 'Intel Core i5-3450',
			'motherboard': 'Gigabyte GA-H61M-DS2',
			'powersupply': 'RAKK 400 watts',
			'rams': '4GB Kingston HyperX Fury DDR4 2400Mhz',
			'size-storage': 'Kingspec -- 120gb',
			'fan': 'Allan 12V Fan -- 80mm',
			'graphics-card': 'Colorful GeForce GT730K -- 2gb',
			'pc_case': 'Rakk Marug -- MicroATX',})

		self.assertEqual(Build.objects.count(), 1)

		newBuild = Build.objects.first()

		self.assertEqual(newBuild.builder_info.username, 'Silver')
		self.assertEqual(newBuild.builder_info, user1)

	def test_redirects_to_list_view(self):
		user1 = User.objects.create(username = 'Silver')
		user2 = User.objects.create(username = 'Adore')

		response = self.client.post(f'/myApp/addlist/{user1.id}/',
			{'budget_': 10000,
			'1model-processesor': 'Intel Core i5-3450',
			'motherboard': 'Gigabyte GA-H61M-DS2',
			'powersupply': 'RAKK 400 watts',
			'rams': '4GB Kingston HyperX Fury DDR4 2400Mhz',
			'size-storage': 'Kingspec -- 120gb',
			'fan': 'Allan 12V Fan -- 80mm',
			'graphics-card': 'Colorful GeForce GT730K -- 2gb',
			'pc_case': 'Rakk Marug -- MicroATX',})

		self.assertRedirects(response, f'/myApp/buildlist/{user1.id}/')

