from flask import Flask, render_template, request, Response
app = Flask(__name__)

@app.route('/')
def inputdata():
   sample_structure = """
{
   "name": str,
   "email": str,
   "username": str,
}
"""

   return render_template('builder.html', sample_structure=sample_structure)

@app.route('/result',methods = ['POST'])
def final_data():
   if request.method == 'POST':
      path_name = request.form["object/entity_name"]
      structure_format = request.form["structure"]
      with open("boilerplate_template.py", "r") as f:
         data = f.read()
         data = data.replace("entity", path_name)
         data = data.replace("sample_structure", structure_format)
      with open("boilerplate.py", "w") as f:
         f.write(data)
      return Response(
         data,
         mimetype="text/py",
         headers={"Content-disposition":
                     "attachment; filename=boilerplate.py"})


if __name__ == '__main__':
   app.run(debug = True)