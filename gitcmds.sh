git clone https://github.com/shirleynelson/shirleynelsonhub.git
cd shirleynelsonhub
cat "<!DOCTYPE html><html><head><title>Test1</title></head><body>Hello Hello</body></html>" > hello.html 
git add hello.html
git commit -m "Add mini hello html"
git push
git status 
git log
git reset --hard 574213db866d486ffb7391baffbd42c04c9334dc
