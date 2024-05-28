from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4
        b = 1
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5
        assert result == expected
        
    def test_subtract(self):
        #Arrange
        a = 4
        b = 1
        cal = Calculator()

        # Act
        result = cal.subtract(a, b)

        # Assert
        expected = 3
        assert result == expected

    def test_multiply(self):
        # Arrange
        a = 4
        b = 1
        cal = Calculator()

        # Act
        result = cal.multiply(a, b)

        # Assert
        expected = 4
        assert result == expected
        
    def test_divide(self):
        # Arrange
        a = 4
        b = 2
        cal = Calculator()

        # Act
        result = cal.divide(a, b)

        # Assert
        expected = 2
        assert result == expected


    




