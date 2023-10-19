#include <iostream>
#include <string>
#include <regex>

bool isProperFunctionDeclaration(const std::string& line) {
    std::regex pattern(R"(\s*\w+\s+\w+\s*\([^)]*\);)");
    return std::regex_match(line, pattern);
}

bool isProperFunctionDefinition(const std::string& line) {
    std::regex pattern(R"(\s*\w+\s+\w+\s*\([^)]*\)\s*\{[^}]*\};)");
    return std::regex_match(line, pattern);
}

int main() {
    std::string input = "int add(int a, int b)";
    std::string input2 = "int add(int a, int b) { return a + b; }";

    bool isDeclaration = isProperFunctionDeclaration(input);
    bool isDefinition = isProperFunctionDefinition(input2);

    if (isDeclaration) {
        std::cout << "Proper function declaration: " << input << std::endl;
    }
    if (isDefinition) {
        std::cout << "Proper function definition: " << input2 << std::endl;
    }
    if (!isDeclaration && !isDefinition) {
        std::cout << "Not a proper function declaration or definition." << std::endl;
    }
    return 0;
}
