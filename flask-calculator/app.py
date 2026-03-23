from flask import Flask, request, jsonify
import ast
import operator

app = Flask(__name__)

# Supported operators
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}

def eval_expr(node):
    """Safely evaluate an arithmetic expression AST."""
    if isinstance(node, ast.Expression):
        return eval_expr(node.body)
    elif isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    elif isinstance(node, ast.BinOp):
        op = OPERATORS[type(node.op)]
        left = eval_expr(node.left)
        right = eval_expr(node.right)
        return op(left, right)
    elif isinstance(node, ast.UnaryOp):
        op = OPERATORS[type(node.op)]
        operand = eval_expr(node.operand)
        return op(operand)
    else:
        raise ValueError("Unsupported expression")

@app.route('/calculate', methods=['POST'])
def calculate():
    """POST endpoint to evaluate arithmetic expressions."""
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON payload"}), 400

    if not data or 'expression' not in data:
        return jsonify({"error": "Expression field is required"}), 400

    expr = str(data['expression']).strip()

    if not expr:
        return jsonify({"error": "Expression cannot be empty"}), 400

    try:
        # Parse the expression into AST
        tree = ast.parse(expr, mode='eval')

        # Safely evaluate the expression
        result = eval_expr(tree)

        # Ensure the result is a number
        if not isinstance(result, (int, float)):
            return jsonify({"error": "Expression did not evaluate to a number"}), 400

        return jsonify({"result": result}), 200

    except ZeroDivisionError:
        return jsonify({"error": "Division by zero"}), 400
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as ex:
        return jsonify({"error": f"Invalid expression: {str(ex)}"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

# Sample cURL test commands:
# Valid arithmetic operations:
# curl -X POST http://localhost:5000/calculate -H "Content-Type: application/json" -d '{"expression": "2 + 3 * 4"}'
# curl -X POST http://localhost:5000/calculate -H "Content-Type: application/json" -d '{"expression": "(5 + 3) * 2"}'
# curl -X POST http://localhost:5000/calculate -H "Content-Type: application/json" -d '{"expression": "2**10"}'
# curl -X POST http://localhost:5000/calculate -H "Content-Type: application/json" -d '{"expression": "-15 * 3"}'
#
# Error cases:
# curl -X POST http://localhost:5000/calculate -H "Content-Type: application/json" -d '{"expression": "5 / 0"}'
# curl -X POST http://localhost:5000/calculate -H "Content-Type: application/json" -d '{"expression": "invalid syntax"}'
# curl -X POST http://localhost:5000/calculate -H "Content-Type: application/json" -d '{}'
