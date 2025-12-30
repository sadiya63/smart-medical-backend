const express = require('express');
const router = express.Router();
const Appointment = require('../models/Appointment');

router.get('/book', (req, res) => {
  res.send('GET route is working: Appointment booking endpoint');
});

router.post('/book', async (req, res) => {
  try {
    const { fullName, doctor, date, time } = req.body;

    
    if (!fullName || !doctor || !date || !time) {
      return res.status(400).json({ error: 'Please provide all required fields' });
    }
    const newAppointment = new Appointment({ fullName, doctor, date, time });
    await newAppointment.save();

    console.log('📨 Appointment booked:', req.body);
    res.status(201).json({ message: 'Appointment booked successfully' });
  } catch (error) {
    console.error('❌ Error booking appointment:', error);
    res.status(500).json({ error: 'Server error' });
  }
});

router.get('/', async (req, res) => {
  try {
    const appointments = await Appointment.find().sort({ createdAt: -1 });
    res.json(appointments);
  } catch (error) {
    console.error('❌ Error fetching appointments:', error);
    res.status(500).json({ error: 'Server error' });
  }
});

module.exports = router;
