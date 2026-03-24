import project as p
import string as s
import os


# Test 1: For generate_password
def test_generate_password():
    pwd = p.generate_password(25)
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_punctuation = any(c in s.punctuation for c in pwd)
    assert len(pwd) == 25
    assert has_upper and has_lower and has_digit and has_punctuation

# Test 2: For evaluate_strength
def test_evaluate_strength():
    assert p.evaluate_strength("Pepo@741@852") == "Strong"
    assert p.evaluate_strength("Pe@741@852") == "Moderate"
    assert p.evaluate_strength("Pep") == "Weak"

# Test 3: For save_to_file
def test_save_to_file():
    test_file = "test_data.txt"
    p.save_to_file("secret123", "Gmail", filename=test_file)
    assert os.path.exists(test_file)
    with open(test_file, "r") as f:
        assert "Gmail: secret123" in f.read()
    os.remove(test_file)