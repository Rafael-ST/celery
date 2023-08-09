from celery import shared_task
from time import sleep

@shared_task
def export_data_to_csv(lista):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dados_exportados.csv"'
    writer = csv.writer(lista)
    print(lista)
    print('###########################')

    # Escreva cabeçalhos
    writer.writerow(['Nome'])

    # Escreva os dados
    for obj in lista:
        writer.writerow([obj.nome])
    return response

@shared_task
def simple_task(message):
    sleep(5)  # Simula algum trabalho demorado
    return f"Task completed: {message}"

@shared_task
def sharedtask():
    return