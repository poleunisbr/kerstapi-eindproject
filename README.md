# Kerst API

## Over mij

Studentennummer: r0931795

Naam: Bryan Poleunis

## Beschrijving/Thema

Ik heb gekozen voor het thema Kerstmis omdat deze opdracht viel tijdens de feestdagen en ik me bevond in de kerstsfeer bij mij thuis en op bezoek bij familieleden.
In deze repo vind je mij REST api waarmee je users kan aanmaken om in te loggen om de rest van de api te kunnen gebruiken, voor de rest heeft mijn api een aantal endpoint in verband met kerstmarkten, kerstdecoraties en kerstgerechten deze zal ik later overlopen in deze file.

## Okteto cloud

Deze API is gehost op Okteto Cloud. Je kunt de API-documentatie en voorbeelden vinden op de volgende locatie:

[API](https://kerst-api-poleunisbr.cloud.okteto.net)

[Documentatie](https://kerst-api-poleunisbr.cloud.okteto.net/docs)

De API maakt gebruik van standaard authenticatie voor sommige endpoints om in te loggen voor gebruik je volgende credentials:

USERNAME: administrator

PASSWORD: admin-api

## Aantoonbare Werking

Hieronder vind je een aantal voorbeelden van Postman-verzoeken die elk endpoint van de API demonstreren.

### Teams Endpoints

#### 1. Een nieuw team maken

![Create Team](/scr/teamsPost.png)

#### 2. Een specifiek team ophalen

![Get Team](/scr/teamsGetID.png)

#### 3. Alle teams ophalen

![Get Teams](/scr/teamsGet.png)

#### 4. Een bestaand team bijwerken

![Update Team](/scr/teamsPut.png)

#### 5. Een team verwijderen

![Delete Team](/scr/teamsDelete.png)

### Scores Endpoints

#### 1. Een nieuwe score toevoegen

![Create Score](/scr/scoresPost.png)

#### 2. Een specifieke score ophalen

![Get Score](/scr/scoresGetID.png)

#### 3. Alle scores ophalen

![Get Scores](/scr/scoresGet.png)

#### 4. Een bestaande score bijwerken

![Update Score](/scr/scoresPut.png)

#### 5. Een score verwijderen

![Delete Score](/scr/scoresDelete.png)

# Volledige OpenAPI Docs

Hier is een screenshot van de volledige OpenAPI-docs pagina:

![OpenAPI Documentatie](/scr/endpoints.png)

## Endpoints

Hieronder vind je gedetailleerde informatie over elk individueel endpoint van de Voetbal API.

### 1. Weergeven Alle Teams

**Endpoint:** `/teams/`

**Methode:** `GET`

Dit endpoint geeft een lijst met alle voetbalteams.

![Get Teams](/scr/teamsGetEndpoint.png)

### 2. Een Nieuw Team Maken

**Endpoint:** `/teams/`

**Methode:** `POST`

Dit endpoint maakt een nieuw voetbalteam aan.

![Create Team](/scr/teamsPostEndpoint.png)

### 3. Een Specifiek Team Ophalen

**Endpoint:** `/teams/{team_id}`

**Methode:** `GET`

Dit endpoint haalt informatie op over een specifiek voetbalteam op basis van het team ID.

![Get Team](/scr/teamsGetIDEndpoint.png)

### 4. Een Team Bijwerken

**Endpoint:** `/teams/{team_id}`

**Methode:** `PUT`

Dit endpoint werkt de informatie van een specifiek voetbalteam bij op basis van het team ID.

![Update Team](/scr/teamsPutEndpoint.png)

### 5. Een Team Verwijderen

**Endpoint:** `/teams/{team_id}`

**Methode:** `DELETE`

Dit endpoint verwijdert een specifiek voetbalteam op basis van het team ID.

![Delete Team](/scr/teamsDeleteEndpoint.png)

### 6. Weergeven Alle Scores

**Endpoint:** `/scores/`

**Methode:** `GET`

Dit endpoint geeft een lijst met alle scores.

![Get Scores](/scr/scoresGetEndpoint.png)

### 7. Een Nieuwe Score Toevoegen

**Endpoint:** `/scores/`

**Methode:** `POST`

Dit endpoint voegt een nieuwe score toe.

![Create Score](/scr/scoresPostEndpoint.png)

### 8. Een Specifieke Score Ophalen

**Endpoint:** `/scores/{score_id}`

**Methode:** `GET`

Dit endpoint haalt informatie op over een specifieke score op basis van het score ID.

![Get Score](/scr/scoresGetIDEndpoint.png)

### 9. Een Score Bijwerken

**Endpoint:** `/scores/{score_id}`

**Methode:** `PUT`

Dit endpoint werkt de informatie van een specifieke score bij op basis van het score ID.

![Update Score](/scr/scoresPutEndpoint.png)

### 10. Een Score Verwijderen

**Endpoint:** `/scores/{score_id}`

**Methode:** `DELETE`

Dit endpoint verwijdert een specifieke score op basis van het score ID.

![Delete Score](/scr/scoresDeleteEndpoint.png)
