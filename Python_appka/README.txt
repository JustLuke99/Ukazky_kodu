Nainstalování závislostí: "pip install -r requirements.txt"
Program se spustí příkazem: "python manage.py runserver"

přístupné ENDPOINTY:
    [POST] /import - Nahrání dat do databáze.
    [GET] /detail/<nazev modelu>/ - Zobrazení seznamu zadaných modelů.
    [GET] /detail/<nazev modelu>/<id> - Zobrazení informací konkrétního záznamu.
    [GET] /del - Smazání celé databáze. 
    /admin - Pro zobrazení databáze (user: admin, pw: admin).