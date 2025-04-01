document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("calculate").addEventListener("click", async function (event) {
      event.preventDefault(); // Prevent default form submission

      // Get values from input fields
      const alicePrivateKey = document.getElementById("alicePrivateKeyInput").value;
      const bobPrivateKey = document.getElementById("bobPrivateKeyInput").value;
      const agreedG = document.getElementById("agreedGInput").value;
      const agreedPrimeNumber = document.getElementById("agreedPrimeNumberInput").value;

      // Ensure all fields are filled
      if (!alicePrivateKey || !bobPrivateKey || !agreedG || !agreedPrimeNumber) {
          alert("Please fill in all required fields.");
          return;
      }

      // Create JSON object to send
      const requestData = {
          alicePrivateKey: parseInt(alicePrivateKey, 10),
          bobPrivateKey: parseInt(bobPrivateKey, 10),
          agreedG: parseInt(agreedG, 10),
          agreedPrimeNumber: parseInt(agreedPrimeNumber, 10),
      };

      try {
          // Send data to backend
          const response = await fetch("http://localhost:8080/compute", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify(requestData),
          });

          // Handle response
          if (!response.ok) {
              throw new Error("Failed to fetch response from server.");
          }

          const responseData = await response.json();
          if(responseData.message)
            alert(responseData.message);

          console.log("Full Response:", responseData);

          // Update the UI with received data
          document.getElementById("alicePublicKey").textContent = responseData.alicePublicKey;
          document.getElementById("bobPublicKey").textContent = responseData.bobPublicKey;
          document.getElementById("aliceSharedSecret").textContent = responseData.sharedSecret;
          document.getElementById("bobSharedSecret").textContent = responseData.sharedSecret;

      } catch (error) {
          console.error("Error:", error);
          alert("An error occurred. Please try again.");
      }
  });
});
