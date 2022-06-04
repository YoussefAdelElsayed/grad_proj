function getBotResponse(input) {
    //rock paper scissors
    if (input == "rock") {
        return "paper";
    } else if (input == "paper") {
        return "scissors";
    } else if (input == "scissors") {
        return "rock";
    }

    // Simple responses
    if (input == "hello") {
        return "welcome in FCI website";
    } else if (input == "goodbye") {
        return "talk to you later";
    } else if (input == "what is the full form of FCI ?") {
        return "Faculty of Computer and Information";
    } else if (input == "what are the departments in FCI ?") {
        return "1)CS 2)IT 3)SE 4)AI";
    } else if (input == "what is the full form of CS ?") {
        return "Computer Science";
    } else if (input == "what is the full form of IT ?") {
        return "Information Technology";
    } else if (input == "what is the full form of SE ?") {
        return "Software Engineering";
    } else if (input == "what is the full form of AI ?") {
        return "Artificial Intelligence";
    } else {
        return "try asking something else !";
    }
}