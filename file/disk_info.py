import psutil


def print_disk_info():
    disk_info = []
    for part in psutil.disk_partitions(all=True):
        if psutil.WINDOWS:
            # пропуск несмонтированных дисков во избежании ошибок
            # при запуске на Windows
            if part.fstype == '':
                disk_info.append({
                    'Диск': part.device,
                    'Тип': part.opts,
                    'Готов': False
                })
                continue

        usage = psutil.disk_usage(part.mountpoint)
        disk_info.append({
            'Диск': part.mountpoint,
            'Тип': part.opts,
            'Файловая система': part.fstype,
            'Всего': usage.total,
            'Использовано': usage.used,
            'Использовано %': usage.percent,
            'Свободно': usage.free
        })

    for part in disk_info:
        for key, value in part.items():
            print(f"{key}: {value}")
        print("---------------")


print_disk_info()