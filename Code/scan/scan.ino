unsigned long previousMillis = 0;  // Stores the last time "Hello" was printed
const long interval = 10000;       // Interval at which to print "Hello" (10 seconds)

void setup() {
    // Initialize serial communication at a baud rate of 115200
    Serial.begin(115200);
    
    // Wait for serial port to connect
    while (!Serial) {
        ; // Wait for serial port to connect. Needed for native USB
    }

    // Print initial message
    Serial.println("Hello");
}

void loop() {
    unsigned long currentMillis = millis();  // Get the current time

    // Check if 10 seconds have passed
    if (currentMillis - previousMillis >= interval) {
        previousMillis = currentMillis;  // Save the last time "Hello" was printed
        
        // Print "Hello" to the serial monitor
        Serial.println("Hello");
    }
}
