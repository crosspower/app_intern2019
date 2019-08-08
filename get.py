import services
import os
from importlib import import_module

def services_scrape(word):
    # servicesディレクトリにあるサービス一覧を取得
    service_names = list(filter(lambda file_name: not ("__" in file_name), os.listdir('services')))
    service_names = [service.replace(".py","") for service in service_names]

    result = []
    for service_name in service_names:
        module = import_module("services."+service_name)
        
        result.append(dict(
                service = service_name,
                item = module.scrape(word)
            ))
    return result

if __name__ == "__main__":
    services_scrape()