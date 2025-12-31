const express = require("express");
const axios = require("axios");
const router = express.Router();

router.post("/", async (req, res) => {
  try {
    axios.post("https://smart-medical-chatbot.onrender.com/chat", {
    message: req.body.message,
    });
    res.json({ reply: response.data.reply });
  } catch (err) {
    res.status(500).json({ reply: "Chatbot service unavailable" });
  }
});

module.exports = router;
