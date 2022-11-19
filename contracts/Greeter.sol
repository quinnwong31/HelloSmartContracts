pragma solidity ^0.5.0;

contract Greeter { 
    string public greeting;

    function Greeter() public { 
        greeter = "Hello";
    }

    function setGreeting(string _greeting) public { 
        greeting = _greeting;
    }

    function greet() view public returns (string) { 
        return greeting;
    }
}