from analyzer.analyzer import analyze_request


requests=[
"""
Siamo una piccola azienda e vorremmo un'app per aiutare i nostri
clienti a gestire i loro ordini. Dovrebbe essere semplice da usare
e accessibile sia da computer che da smartphone.

Vorremmo ricevere una prima stima del progetto.
""",

"""
Un'azienda di 15 dipendenti vuole un piccolo sito web per mostrare
i propri prodotti. Il sito avrà circa 5 pagine e un modulo di contatto.

Non sono necessari account utente, pagamenti o applicazioni mobile.

Tuttavia, il modulo di contatto deve essere integrato con Salesforce
e ogni richiesta deve essere automaticamente associata al corretto
account cliente presente nel CRM.
""",

"""
Vogliamo sviluppare un e-commerce per un'azienda che vende circa
2.000 prodotti.

Il sistema deve permettere ai clienti di registrarsi, cercare e
filtrare i prodotti, aggiungerli al carrello e acquistare online.

Sono richiesti:
- pagamenti con carta e PayPal
- gestione degli ordini
- email di conferma
- area personale del cliente
- pannello amministrativo per gestire prodotti e ordini
- codici sconto
- gestione delle quantità disponibili in magazzino

Il sito deve essere responsive e supportare italiano e inglese.
""",

"""
Una società di logistica vuole sviluppare una piattaforma utilizzata
da circa 2.000 autisti e 300 operatori.

Gli autisti utilizzeranno un'app mobile per ricevere le consegne,
aggiornare lo stato delle spedizioni e condividere la propria posizione
in tempo reale.

Gli operatori utilizzeranno una dashboard web per monitorare tutti
i veicoli su una mappa e assegnare nuove consegne.

Il sistema deve:
- aggiornare le posizioni in tempo reale
- funzionare anche con connessione intermittente
- inviare notifiche push
- integrarsi con il gestionale SAP esistente
- gestire ruoli e permessi
- mantenere uno storico completo delle attività
- essere disponibile 24/7
- supportare almeno 1.000 utenti contemporaneamente
""",
"""
Vorremmo sviluppare una piattaforma web per i nostri 10.000 clienti.

Ogni cliente deve poter creare un account e accedere alla propria
area personale.

La piattaforma dovrà essere estremamente semplice e non dovrà
contenere funzionalità complesse.

Tuttavia, dovrà anche includere:
- autenticazione a due fattori
- integrazione con tre sistemi esterni
- pagamenti ricorrenti
- dashboard personalizzate
- report avanzati
- sistema di notifiche
- API pubbliche
- gestione di ruoli e permessi
- audit log
- supporto multilingua

Il progetto dovrebbe essere completato in circa due settimane.
""",

"""
Siamo un'azienda di circa 200 dipendenti e vogliamo sviluppare
una piattaforma interna per la gestione delle trasferte aziendali.

I dipendenti devono poter:
- creare una richiesta di trasferta
- specificare destinazione, date e motivazione
- caricare ricevute
- visualizzare lo stato della richiesta

I responsabili devono poter approvare o rifiutare le richieste.

Il reparto amministrativo deve poter visualizzare tutte le trasferte
e scaricare un report mensile.

Il sistema dovrà inviare notifiche email quando una richiesta viene
creata, approvata o rifiutata.

La piattaforma sarà accessibile esclusivamente dalla rete aziendale.
"""
]

for i, request in enumerate(requests, start=1):
    print(f"\n\n==============SCENARIO {i}======================\n")
    result = analyze_request(request)

    print("\nPROJECT TYPE:")
    print(result.project_type)

    print("\nSUMMARY:")
    print(result.summary)

    print("\nREQUIREMENTS:")
    for requirement in result.requirements:
        print(f"- {requirement}")

    print("\nCOMPLEXITY:")
    print(result.complexity)

    print("\nMISSING INFORMATION:")
    for information in result.missing_information:
        print(f"- {information}")

    print("\nCLARIFYING QUESTIONS:")
    for question in result.clarifying_questions:
        print(f"- {question}")

    print("\nESTIMATED EFFORT:")
    print(
        f"{result.estimated_effort.min_hours}"
        f"-"
        f"{result.estimated_effort.max_hours} hours"
    )

    print("\nASSUMPTIONS:")
    for assumption in result.assumptions:
        print(f"- {assumption}")

    print("\nCONFIDENCE:")
    print(result.confidence)

