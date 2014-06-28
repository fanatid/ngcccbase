import os


def system(cmd):
    print cmd
    os.system(cmd)

def main():
    system('pyrcc4 icons.qrc -o ui/ui_files/icons_rc.py')

    system('pyuic4 ui/forms/addassetdialog.ui   -o ui/ui_files/addassetdialog_ui.py')
    system('pyuic4 ui/forms/qtui.ui             -o ui/ui_files/qtui_ui.py')
    system('pyuic4 ui/forms/assetspage.ui       -o ui/ui_files/assetspage_ui.py')
    system('pyuic4 ui/forms/historypage.ui      -o ui/ui_files/historypage_ui.py')
    system('pyuic4 ui/forms/issuedialog.ui      -o ui/ui_files/issuedialog_ui.py')
    system('pyuic4 ui/forms/newaddressdialog.ui -o ui/ui_files/newaddressdialog_ui.py')
    system('pyuic4 ui/forms/receivepage.ui      -o ui/ui_files/receivepage_ui.py')
    system('pyuic4 ui/forms/sendcoinsentry.ui   -o ui/ui_files/sendcoinsentry_ui.py')
    system('pyuic4 ui/forms/sendcoinspage.ui    -o ui/ui_files/sendcoinspage_ui.py')
    system('pyuic4 ui/forms/tradepage.ui        -o ui/ui_files/tradepage_ui.py')


if __name__ == '__main__':
    main()
