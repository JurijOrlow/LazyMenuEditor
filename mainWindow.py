import main

class mainWindow(main.Gtk.Window):
    def handler(self, widget):
        self.mainBox.destroy()
        self.scroll.destroy()
        self.generateList(self)
        self.show_all()

    def generateList(self, widget):
        self.scroll = main.Gtk.ScrolledWindow()
        self.scroll.set_policy (main.Gtk.PolicyType.NEVER, main.Gtk.PolicyType.AUTOMATIC)
        self.mainBox = main.Gtk.Box(orientation = main.Gtk.Orientation.VERTICAL)
        list = main.sp.getoutput('ls /home/$USER/.local/share/applications/').split('\n')
        #print(list)
        for i in list:
            #print(i)
            itemBox = main.Gtk.Box(orientation = main.Gtk.Orientation.HORIZONTAL)
            itemLabel = main.Gtk.Label(label = i)
            itemLabel.set_halign(main.Gtk.Align.START)

            itemMore = main.Gtk.Button()
            itemMore.add(main.Gtk.Arrow(arrow_type = main.Gtk.ArrowType.RIGHT))
            itemMore.connect("clicked", self.editItem, i)
            itemMore.set_halign(main.Gtk.Align.END)

            itemDel = main.Gtk.Button(label = "Delete")
            itemDel.connect("clicked", self.deleteItem, i)
            itemDel.set_halign(main.Gtk.Align.END)

            itemBox.pack_start(itemLabel, True, True, 20)
            itemBox.add(itemDel)
            itemBox.add(itemMore)

            self.mainBox.add(itemBox)
            self.mainBox.add(main.Gtk.Separator(orientation = main.Gtk.Orientation.HORIZONTAL))
            self.mainBox.add(main.Gtk.Separator(orientation = main.Gtk.Orientation.HORIZONTAL))
        self.scroll.add(self.mainBox)
        self.add(self.scroll)


    def deleteItem(self, widget, element):
        str = "Deleted entry " + element
        user = main.sp.getoutput('echo $USER')
        command = "rm \'/home/" + user + "/.local/share/applications/" + element + "\'"
        main.os.popen(command)
        n = main.Notify.Notification.new("Lazy Menu Editor", str)
        n.show()
        self.handler(self)

    def editItem(self, widget, element=".tmp"):
        editItemWindow = editItem(element)
        editItemWindow.connect("destroy", self.handler)
        editItemWindow.show_all()

    def __init__(self):
        main.Gtk.Window.__init__(self, title="Lazy Menu Editor")
        main.Gtk.Window.set_default_size(self, 450,250)

        main.Notify.init("Lazy Menu Editor")
        header = main.Gtk.HeaderBar()
        header.set_show_close_button(True)
        header.props.title = "Lazy Menu Editor"
        self.set_titlebar(header)

        box = main.Gtk.Box(orientation=main.Gtk.Orientation.HORIZONTAL)

        button = main.Gtk.Button(label = "New Item")
        button.connect("clicked", self.editItem)
        box.add(button)
        header.pack_start(box)

        self.generateList(self)
