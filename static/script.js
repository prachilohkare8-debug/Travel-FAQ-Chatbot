const chatBox = document.getElementById("chat-box");
const input = document.getElementById("message");
const sendBtn = document.getElementById("send-btn");

// Display current time
function getCurrentTime() {

    const now = new Date();

    return now.toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });

}

// Add message to chat
function addMessage(text, sender) {

    const message = document.createElement("div");

    message.className = `message ${sender}`;

    message.innerHTML = `

        <div class="bubble">

            ${text}

        </div>

        <span class="time">

            ${getCurrentTime()}

        </span>

    `;

    chatBox.appendChild(message);

    chatBox.scrollTop = chatBox.scrollHeight;

}

// Typing animation
function showTyping() {

    const typing = document.createElement("div");

    typing.className = "message bot";

    typing.id = "typing";

    typing.innerHTML = `

        <div class="bubble">

            Bot is typing...

            <div class="typing">

                <span></span>

                <span></span>

                <span></span>

            </div>

        </div>

    `;

    chatBox.appendChild(typing);

    chatBox.scrollTop = chatBox.scrollHeight;

}

function removeTyping() {

    const typing = document.getElementById("typing");

    if (typing) {

        typing.remove();

    }

}

// Send message
async function sendMessage() {

    const message = input.value.trim();

    if (message === "") return;

    addMessage(message, "user");

    input.value = "";

    input.focus();

    showTyping();

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                message: message

            })

        });

        const data = await response.json();

        setTimeout(() => {

            removeTyping();

            addMessage(data.reply, "bot");

        }, 800);

    }

    catch (error) {

        removeTyping();

        addMessage(
            "Something went wrong. Please try again.",
            "bot"
        );

    }

}

// Suggested questions
function fillQuestion(question) {

    input.value = question;

    sendMessage();

}

// Send button
sendBtn.addEventListener("click", sendMessage);

// Enter key
input.addEventListener("keypress", function(event) {

    if (event.key === "Enter") {

        sendMessage();

    }

});

// Welcome message
window.onload = function () {

    addMessage(

`👋 Welcome to the Travel FAQ Chatbot!

I can answer questions about:

✈️ Flight Booking

🏨 Hotel Booking

🛄 Baggage Rules

📄 Passport & Visa

🎫 Ticket Cancellation

💳 Payments & Refunds

Try asking a question or click one of the suggestions above.`,

"bot"

    );

};