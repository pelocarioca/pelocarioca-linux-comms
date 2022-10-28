#include <iostream>
using namespace std;

/*No me dejen tocar un ordenador*/
/*Clase que gestiona las operaciones*/
class operacion {
	public:
		/*
		nom1 : nombre de la 1a parte de la op,
		nom2 : nombre de la 2a parte de la op,
		operador : operador de la op,
		val1 : primer valor del cálculo,
		val2 : segundo valor del cálculo
		*/
		string nom1;
		string nom2;
		string operador;
		int val1;
		int val2;

		/*El constructor*/
		operacion(string vnom1, string vnom2, string voperador) {
			nom1 = vnom1;
			nom2 = vnom2;
			operador = voperador;

			cout << "Ingrese primero, "
				<< nom1
				<< ": ";
			cin >> val1;

			cout << "Ingrese segundo, "
				<< nom2
				<< ": ";
			cin >> val2;

			/*La peor forma de formatear un string :)*/
			cout << val1
				<< " " << operador << " "
				<< val2
				<< " = ";

			/*Se hace el cálculo*/
			calculo(val1, val2);

		}

	/*El cálculo*/
	void calculo(int val1, int val2) {
		if (operador == "+") {
			cout << val1+val2 << endl;
		}
		if (operador == "-") {
			cout << val1-val2 << endl;
		}
		if (operador == "/") {
			cout << (float)val1 / (float)val2 << endl;
		}
		if (operador == "*") {
			cout << val1*val2 << endl;
		}

		/*Salida exitosa del programa*/
		exit( 0 );

	}
};

/*Inicio del programa*/
int main() {
	string i;

	cout << "Ingrese operación (suma, resta, multiplicación, división): ";
	cin >> i;

	if ( i == "suma" ) { operacion ops("sumando", "sumando", "+"); }
	if ( i == "resta" ) { operacion opr("minuendo", "sustraendo", "-"); }
	if ( i == "multiplicación" ) { operacion opm("multiplicando", "multiplicador", "*"); }
	if ( i == "división" ) { operacion opd("dividendo", "divisor", "/"); }

	/*Si no se elige ninguno válido vuelve a empezar (no se gestionar memoria)*/
	cout << i << " no es una operación permitida >:(" << endl;
	main();

}
