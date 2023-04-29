curl 'https://api.mendeley.com/search/catalog?query=whales' \
-X GET \
-H 'Authorization: Bearer MTUxNzM6R1VWbUl2UzRjMkdEY2RUYQ==' \
-H 'Accept: application/vnd.mendeley-document.1+json'

curl 'https://api.mendeley.com/oauth/token' \
-X POST \
-H 'Authorization: Basic MTUxNzM6R1VWbUl2UzRjMkdEY2RUYQ==' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'grant_type=client_credentials&scope=all' 