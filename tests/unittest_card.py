import unittest
from my_package.card import BingoCard


class TestBingoCard(unittest.TestCase):

    def test_grid_dimensions(self):
        # La tarjeta debe tener rows x cols elementos.
        rows, cols = 3, 7  # definimos unos parámetros de ejemplo para probar
        card = BingoCard(rows=rows, cols=cols, max_number=99)  # creamos la tarjeta

        # comprobamos que el número de filas es correcto
        self.assertEqual(len(card.grid), rows)
        # comprobamos que cada fila tiene el número correcto de columnas
        for row in card.grid:
            self.assertEqual(len(row), cols)

    def test_numbers_unique_and_in_range(self):
        # Todos los números deben ser únicos y estar dentro del rango permitido.
        rows, cols, max_number = 3, 7, 50  # max_number, rows y cols para que random.sample funcione
        card = BingoCard(rows=rows, cols=cols, max_number=max_number)  # generamos una tarjeta

        nums = [n for row in card.grid for n in row]  # aplanamos el grid para analizarlo

        # tamaño correcto, debe haber exactamente rows * cols números
        self.assertEqual(len(nums), rows * cols)

        # unicidad, si convertimos a set() no debe perder elementos
        self.assertEqual(len(set(nums)), len(nums))

        # rango, todos los números deben estar entre 1 y max_number
        self.assertTrue(all(1 <= n <= max_number for n in nums))

    def test_card_is_sorted_row_wise(self):
        # Como se aplica sort() antes de dividir en filas, la tarjeta debe quedar ordenada.
        # Esto significa que, si la leemos como una lista plana, debe coincidir con sorted().
        card = BingoCard(rows=3, cols=7, max_number=99)  # generamos una tarjeta de ejemplo

        flat = [n for row in card.grid for n in row]  # convertimos la tarjeta en una lista única
        self.assertEqual(flat, sorted(flat))  # comprobamos que está realmente ordenada

    def test_mark_number_marks_and_returns_true(self):
        # Si el número está en la tarjeta, mark_number debe marcarlo y devolver True.
        card = BingoCard(rows=3, cols=7, max_number=99)  # creamos una tarjeta de ejemplo

        target = card.grid[0][0]  # elegimos un número que seguro está en la tarjeta
        result = card.mark_number(target)  # intentamos marcarlo

        # comprobamos que mark_number devuelve True al marcar un número existente
        self.assertTrue(result)
        # comprobamos que la casilla correspondiente queda marcada
        self.assertTrue(card.marked[0][0])
        # comprobamos que el número aparece también en marked_set
        self.assertIn(target, card.marked_set)

    def test_mark_number_twice_returns_false(self):
        # Marcar el mismo número dos veces: la primera debe devolver True y la segunda False.
        card = BingoCard(rows=3, cols=7, max_number=99)  # generamos una tarjeta de ejemplo
        target = card.grid[0][0]  # escogemos un número que seguro está en la tarjeta

        first = card.mark_number(target)   # primera vez que marcamos → debería ser True
        second = card.mark_number(target)  # segunda vez → debería ser False

        # comprobamos que la primera llamada devuelve True
        self.assertTrue(first)
        # comprobamos que la segunda devuelve False
        self.assertFalse(second)
        # comprobamos que la casilla sigue marcada
        self.assertTrue(card.marked[0][0])
        # comprobamos que el número aparece en el set de marcados
        self.assertIn(target, card.marked_set)

    def test_mark_number_not_on_card_returns_false(self):
        # Si el número no está en la tarjeta, mark_number debe devolver False y no marcar nada.
        card = BingoCard(rows=3, cols=7, max_number=99)  # max_number suficiente grande

        missing = card.max_number + 1  # elegimos un número fuera de rango para asegurar que no está
        result = card.mark_number(missing)  # intentamos marcarlo

        # comprobamos que la función devuelve False para números inexistentes
        self.assertFalse(result)
        # comprobamos que ninguna casilla ha sido marcada
        self.assertTrue(all(not m for row in card.marked for m in row))
        # comprobamos que el número no aparece en marked_set
        self.assertNotIn(missing, card.marked_set)

    def test_marked_set_consistent_with_marked_matrix(self):
        # Los números marcados en 'marked' y en 'marked_set' deben coincidir.
        card = BingoCard(rows=3, cols=7, max_number=99)  # creamos una tarjeta

        # marcamos dos números de forma controlada
        nums_to_mark = [card.grid[0][0], card.grid[1][2]]
        for n in nums_to_mark:
            card.mark_number(n)

        # recogemos los números marcados en la matriz marcada
        matrix_marked = {
            card.grid[r][c]
            for r in range(card.rows)
            for c in range(card.cols)
            if card.marked[r][c]
        }

        # deben ser exactamente los mismos que aparecen en marked_set
        self.assertEqual(matrix_marked, card.marked_set)

    def test_display_rich_does_not_raise(self):
        # display_rich no debe lanzar excepciones al ejecutarse.
        card = BingoCard(rows=3, cols=7, max_number=99)  # creamos una tarjeta

        try:
            card.display_rich()  # simplemente llamamos a la función
        except Exception as e:
            # si se lanza cualquier excepción, el test falla
            self.fail(f"display_rich lanzó una excepción: {e}")


if __name__ == "__main__":
    unittest.main()
