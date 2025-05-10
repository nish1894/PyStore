console.log("✅ updateCart script loaded");




// Function to update cart
async function updateCart(itemId, action) {
  console.log("updateCart called with:", itemId, action);

  try {
    const response = await fetch("/cart/api/update/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
      body: JSON.stringify({ itemId, action }),
    });
  } catch (error) {
    console.error("Error in updateCart:", error);
  }
}



// Function to update cart counter in the navbar
function updateCartCounter(count) {
  const cartCounter = document.getElementById("cart-counter");
  if (cartCounter) {
    cartCounter.textContent = count;
    count =2;
    // Optionally hide/show the counter based on count
    if (count > 0) {
      cartCounter.style.display = "inline-flex";
    } else {
      cartCounter.style.display = "none";
    }
  }
}
