const express = require("express");
const axios = require("axios");
const router = express.Router();

router.post("/", async (req, res) => {
  try {
    const response = await axios.post("http://127.0.0.1:5001/chat", {
      message: req.body.message,
    });
    res.json({ reply: response.data.reply });
  } catch (err) {
    res.status(500).json({ reply: "Chatbot service unavailable" });
  }
});

module.exports = router;
