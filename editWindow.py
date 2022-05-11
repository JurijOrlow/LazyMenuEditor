import main

class editItem(main.main.Gtk.Window):
    fileEntry = main.main.Gtk.Entry()
    nameEntry = main.main.Gtk.Entry()
    typeEntry = main.main.Gtk.Entry()
    execEntry = main.main.Gtk.Entry()
    iconEntry = main.main.Gtk.Entry()

    def saveItem(self, widget, _location, _element):
        if _element == '.tmp':
            str = _location + self.fileEntry.get_text() + ".desktop"
            toWrite = "[Desktop Entry]" + "\nName=" + self.nameEntry.get_text() + "\nType=" + self.typeEntry.get_text() + "\nExec=" + self.execEntry.get_text() + "\nIcon=" + self.iconEntry.get_text()
            #print(toWrite)
            final_file = open(str, 'w')
            final_file.write(toWrite)
            final_file.flush()
            final_file.close()
        else:
            str = _location + _element
            new_str = _location + _element + ".new"
            final_file_r = open(str, 'r')
            final_file_w = open(new_str, 'w')
            for line in final_file_r:
                if "Name=" in line:
                    line = "Name=" + self.nameEntry.get_text() + "\n"
                elif "Type=" in line:
                    line = "Type=" + self.typeEntry.get_text() + "\n"
                elif "Exec=" in line:
                    line = "Exec=" + self.execEntry.get_text() + "\n"
                elif "Icon=" in line:
                    line = "Icon=" + self.iconEntry.get_text() + "\n"
                final_file_w.write(line)
            final_file_w.flush()
            final_file_w.close()
            final_file_r.close()
            command = 'mv ' + new_str + ' ' + str
            main.os.popen(command)

        str = "Entry added " + self.nameEntry.get_text()
        n = main.Notify.Notification.new("Lazy Menu Editor", str)
        n.show()
        self.destroy()

    def __init__(self, element):
        main.main.Gtk.Window.__init__(self, title="Lazy Menu Editor")
        main.main.Gtk.Window.set_default_size(self, 200,150)
        main.Notify.init("Lazy Menu Editor")
        header = main.main.Gtk.HeaderBar()
        header.set_show_close_button(True)
        header.props.title = "Item Edit"
        self.set_titlebar(header)

        box = main.main.Gtk.Box(orientation=main.main.Gtk.Orientation.HORIZONTAL)

        name = ""
        type = "Application"
        exe = ""
        icon = ""
        original_list = []
        location = '/home/' + main.sp.getoutput('echo $USER') + '/.local/share/applications/'
        header.pack_start(box)
        #user = main.sp.getoutput('echo $USER')
        if element != ".tmp":
            str = location + element
            original = open(str, 'r')
            for line in original:
                original_list.append(line.strip('\n'))
            original.close()

            name = [string for string in original_list if 'Name' in string]
            if len(name) == 1: name = name[0].strip('Name=')
            else: name = ""

            type = [string for string in original_list if 'Type' in string]
            if len(type) == 1: type = type[0].strip('Type=')
            else: type = ""

            exe = [string for string in original_list if 'Exec' in string]
            if len(exe) == 1: exe = exe[0].strip('Exec=')
            else: exe = ""

            icon = [string for string in original_list if 'Icon' in string]
            if len(icon) == 1: icon = icon[0].strip('Icon=')
            else: icon = ""

        mainBox = main.main.Gtk.Box(orientation = main.main.Gtk.Orientation.VERTICAL)

        elementBox = main.main.Gtk.Box(orientation = main.main.Gtk.Orientation.HORIZONTAL)
        label = main.main.Gtk.Label(label = "File name")
        #label.set_size_request(80, -1)
        label.set_halign(main.main.Gtk.Align.START)
        self.fileEntry.set_text(element)
        self.fileEntry.set_halign(main.main.Gtk.Align.END)
        elementBox.pack_start(label, True, True, 20)
        elementBox.pack_end(self.fileEntry, True, True, 0)
        mainBox.add(elementBox)

        elementBox = main.main.Gtk.Box(orientation = main.main.Gtk.Orientation.HORIZONTAL)
        label = main.main.Gtk.Label(label = "Name")
        #label.set_size_request(80, -1)
        label.set_halign(main.main.Gtk.Align.START)
        self.nameEntry.set_text(name)
        self.nameEntry.set_halign(main.main.Gtk.Align.END)
        elementBox.pack_start(label, True, True, 20)
        elementBox.pack_end(self.nameEntry, True, True, 0)
        mainBox.add(elementBox)

        elementBox = main.main.Gtk.Box(orientation = main.main.Gtk.Orientation.HORIZONTAL)
        label = main.main.Gtk.Label(label = "Type")
        #label.set_size_request(80, -1)
        label.set_halign(main.main.Gtk.Align.START)
        self.typeEntry.set_text(type)
        self.typeEntry.set_halign(main.main.Gtk.Align.END)
        elementBox.pack_start(label, True, True, 20)
        elementBox.pack_end(self.typeEntry, True, True, 0)
        mainBox.add(elementBox)

        elementBox = main.main.Gtk.Box(orientation = main.main.Gtk.Orientation.HORIZONTAL)
        label = main.main.Gtk.Label(label = "Exec")
        #label.set_size_request(80, -1)
        label.set_halign(main.main.Gtk.Align.START)
        self.execEntry.set_text(exe)
        self.execEntry.set_halign(main.main.Gtk.Align.END)
        elementBox.pack_start(label, True, True, 20)
        elementBox.pack_end(self.execEntry, True, True, 0)
        mainBox.add(elementBox)

        elementBox = main.main.Gtk.Box(orientation = main.main.Gtk.Orientation.HORIZONTAL)
        label = main.main.Gtk.Label(label = "Icon")
        #label.set_size_request(80, -1)
        label.set_halign(main.main.Gtk.Align.START)
        self.iconEntry.set_text(icon)
        self.iconEntry.set_halign(main.main.Gtk.Align.END)
        elementBox.pack_start(label, True, True, 20)
        elementBox.pack_end(self.iconEntry, True, True, 0)
        mainBox.add(elementBox)

        saveButton = main.main.Gtk.Button(label = "Save")
        saveButton.connect("clicked", self.saveItem, location, element)
        saveButton.set_size_request(20,20)
        saveButton.set_halign(main.main.Gtk.Align.END)
        box = main.main.Gtk.Box(orientation = main.main.Gtk.Orientation.HORIZONTAL)
        box.pack_end(saveButton, True, True, 0)

        mainBox.add(box)

        self.add(mainBox)
