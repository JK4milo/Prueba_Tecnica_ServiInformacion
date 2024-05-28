
# **PRUEBA TÉCNICA Servinformación.**

## **Juan Camilo Botero Rendoón**

Está es una prueba técnica para el puesto de Científico De Datos Junior para la empresa Servinformación.

En este código busqué la aproximación más profesional que mis conocimientos en python me dejaron.

Usé la base de datos ["Bone Break Classification Image Dataset"](https://www.kaggle.com/datasets/pkdarabi/bone-break-classification-image-dataset) de Kaggle.

Está base de datos recolecta 10 categorías diferentes de fracturas. El objetivo es desarrollar una red convolusional para clasificar las fracturas.
## **Ejemplos:**
## **Fractura por avulsión**
![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://storage.googleapis.com/kagglesdsdata/datasets/4257126/7394372/Bone%20Break%20Classification/Bone%20Break%20Classification/Avulsion%20fracture/Test/13256_2019_2325_Fig1_HTML_png.rf.09368fddb2da3979a3e1e25a0cac6f45.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20240528%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240528T064338Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=98d10603eb6f09e434c75b9d84b3d0b58368d2f2a51005e2d7e742ee3843e3a44fa5b5dbe15824765dac093a6fcf63e6a18412691cc93a953feee2a029f1659ab9a660cf6b18c9950cb535d68110c46395fdfb099dbb2bb3470c0d343c10066368155f269982a27277554a04296e9daa301d0bb8742a11fcda965151f8b130888d713dea9ed12deed700b658f5f1c8283ed3558536bb7c955862eeabafdf64df60152cf94f40de342ef96e6abec22d8fe74d844d4575d4b6d5f5620bd1d72f8ebc976e7dcb4068c8ac78334d25f2fb4c8b497b5098d3791d535d04bce85b82496ba85071060ef32d930787852f8a360663778216218ccfb9deba162c886da638)

## **Fractura conminuta**
![ffdfd](https://storage.googleapis.com/kagglesdsdata/datasets/4257126/7394372/Bone%20Break%20Classification/Bone%20Break%20Classification/Comminuted%20fracture/Test/IMG-0001-00001_jumbo_jpeg.rf.4af5e7c047bac2007869a5e19663eb77.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20240528%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240528T064533Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=66495992affad6da8d8a36889bdee365c8ed646f06edd97ac6d06c700323070976b666390add1735378fd083a8200c7f285550d9d3646b065a106e9ead85e1e7392d441ee9e90931e84b1aa0f87ef775040a792bb213a153532fb468875968e1b04579cecbd0c4b81432e51d11e7c5309017073f73ab3d4b91ebfc1297be1da9d299d33c700ed746f405d26cfac092367a078e64f3f4fac7e23b65addabb9da7a5dc7f2c845666e0142da6d4fd358fcd3a899e78207eab207cbad6a3f95c9ccb900cb41d265a093d4ed8d06f81017c91d4c25f756da0e11d7621c5185983806b35857fbafc1f8b1a1779eab57622577f6f62c4ff94a9d7bf41987901ac3c0a3a)

## **Instalación.**

Sigue las instrucciones pero clonar el repositorio y probar el modelo.

```bash
git clone https://github.com/JK4milo/Prueba_Tecnica_ServiInformacion.git
  
virtualenv env

source env/Scripts/activate

pip install -r "requirements.txt"

cd app

python.exe main.py
```


## Tutorial de uso.


Una vez la aplicación este corriendo (usualmente tarda un poco la primera vez), verás a la izquierda un arbol de directorios (1) que corresponden a las imagénes que puedes ser usadas para test.


![image](https://github.com/JK4milo/Prueba_Tecnica_ServiInformacion/blob/main/tutorial_assets_readme/PASO1.png)


Una vez selecciones el arbol de ficheros podrás escoger una imagen para la clasificación (2).
Con la imagen seleccionada se desplegara el nombre de su etiqueta (y_true, 3). Por último sólo queda darle al botón "click to predict" (4).

![image](https://github.com/JK4milo/Prueba_Tecnica_ServiInformacion/assets/137455537/baa2d952-640f-4704-9249-4bb9ff53352e)


La primera ejecución suele tardar más que las demás, por lo tanto no desesperes si la clasificación toma du tiempo. La eitqueta (y_pred) aparecerá unos segundos después con los resultados de la clasificación.

![image](https://github.com/JK4milo/Prueba_Tecnica_ServiInformacion/blob/main/tutorial_assets_readme/paso4.png?raw=true)


