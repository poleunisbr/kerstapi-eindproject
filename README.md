# Kerst API

## Over mij

Studentennummer: r0931795

Naam: Bryan Poleunis

## Beschrijving/Thema

Ik heb gekozen voor het thema Kerstmis omdat deze opdracht viel tijdens de feestdagen en ik me bevond in de kerstsfeer bij mij thuis en op bezoek bij familieleden.

In deze repo vind je mij REST api waarmee je users kan aanmaken om in te loggen om de rest van de api te kunnen gebruiken, voor de rest heeft mijn api een aantal endpoints in verband met kerstmarkten, kerstdecoraties en kerstgerechten deze zal ik later overlopen in deze file.

Naast de API vind je ook de testfile die ik geschreven heb om de endpoints te testen deze word ook uitgevoerd in github actions nadat de action om de container te pushen naar docker hub klaar is.

## Okteto cloud

Deze API is gehost op Okteto Cloud. Je kunt de API-documentatie en voorbeelden vinden op de volgende locatie:

[API](https://kerst-api-poleunisbr.cloud.okteto.net)

[Documentatie](https://kerst-api-poleunisbr.cloud.okteto.net/docs)

De API maakt gebruik van Oauth voor sommige endpoints om in te loggen voor gebruik je volgende credentials:

USERNAME: test@test.com

PASSWORD: test

Normaal gezien bestaat deze user als default in de database moest hij er niet in zitten kan je een user aanmaken met een post request naar de /users endpoint.

## Aantoonbare Werking

Hieronder vind je een aantal voorbeelden van Postman-verzoeken die elk endpoint van de API demonstreren.

### Users Endpoints

#### 1. Een nieuwe user aanmaken

![Create User](/scr/post-users.png)

#### 2. De users ophalen

![Get Users](/scr/get-users.png)

### Token Endpoint

#### 1. Authenticatie token opvragen

![Token](/scr/token.png)

### Kerstmarkten Endpoints

#### 1. Een nieuwe Kerstmarkt aanmaken

![Create User](/scr/post-kerstmarkten.png)

#### 2. De Kerstmarkten ophalen

![Get Users](/scr/get-kerstmarkten.png)

#### 3. Een specifieke kerstmarkt ophalen

![Get Users](/scr/get-kerstmarktenID.png)

#### 4. Een bestaande Kerstmarkt aanpassen

![Get Users](/scr/put-kerstmarkten.png)

#### 5. Een Kerstmarkt deleten

![Get Users](/scr/delete-kerstmarkten.png)


### Kerstgerechten Endpoints

#### 1. Een nieuwe kerstgerecht aanmaken

![Create User](/scr/post-kerstgerechten.png)

#### 2. De kerstgerechten ophalen

![Get Users](/scr/get-kerstgerechten.png)

#### 3. Een specifiek kerstgerecht ophalen

![Get Users](/scr/get-kerstgerechtenID.png)

### Kerstdecoratie Endpoints

#### 1. Een nieuwe kerstdecoratie aanmaken

![Create User](/scr/post-kerstdecoratie.png)

#### 2. De kerstdecoraties ophalen

![Get Users](/scr/get-kerstdecoratie.png)

#### 3. Een specifiek kerstdecoratie ophalen

![Get Users](/scr/get-kerstdecoratieID.png)

# Volledige OpenAPI Docs

Hier is een screenshot van de volledige OpenAPI-docs pagina:

![OpenAPI Documentatie](/scr/docs.png)

Voor meer gedetaileerde info kan je de docs pagina bezoeken.
