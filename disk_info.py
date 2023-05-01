import psutil
import os


def disk_info():
    os.system("cls")
    info = []
    for part in psutil.disk_partitions(all=True):
        if psutil.WINDOWS:
            # пропуск несмонтированных дисков во избежании ошибок
            # при запуске на Windows
            if part.fstype == '':
                info.append({
                    'Диск': part.device,
                    'Тип': part.opts,
                    'Готов': False
                })
                continue

        usage = psutil.disk_usage(part.mountpoint)
        info.append({
            'Диск': part.mountpoint,
            'Тип': part.opts,
            'Файловая система': part.fstype,
            'Всего': usage.total,
            'Использовано': usage.used,
            'Использовано %': usage.percent,
            'Свободно': usage.free
        })
    print("\n[Disk information]\n")
    for part in info:
        for key, value in part.items():
            print(f"    {key}: {value}")
        print()
    input("\n\n => Back")
