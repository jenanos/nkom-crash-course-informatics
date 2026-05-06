# Oppgave 1: Hva er et API?

Et API er en avtalt måte for programmer å snakke med andre programmer på.

Tenk slik:

`Vårt program -> API -> annet system -> svar tilbake`

## Begreper

- **URL:** adressen til API-et
- **endpoint:** en bestemt del av API-et
- **GET:** hente data
- **JSON:** vanlig format for svar fra API-er
- **statuskode:** tall som sier om forespørselen gikk bra
- `200` betyr som regel OK
- `404` betyr ofte ikke funnet
- `500` betyr ofte feil hos server

## JSON-eksempel

```json
{
  "navn": "Ola",
  "alder": 42,
  "roller": ["jurist", "saksbehandler"]
}
```

JSON ligner på Python-dictionaries og lister, men JSON er et tekstformat for datautveksling.

## Kjør startkoden

Kjør:

```bash
cd 03-api-prosjekt/startkode
python3 main.py
```
