update_link = 'https://github.com/evembar/webanlauncher/raw/main/update.zip'
vern = 0.11
def get_version(ver):
    if ver < vern:
        return 'update'
    else:
        return 'no update'