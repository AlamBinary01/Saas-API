const express = require('express');
const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth20').Strategy;
const session = require('express-session');
const router = express.Router();
const secretKey = process.env.SECRET_KEY;
const clientID= process.env.GOOGLE_CLIENT_ID
const clientSecret=process.env.CLIENT_SECRET_ID
router.use(session({ secret: secretKey, resave: true, saveUninitialized: true }));
router.use(passport.initialize());
router.use(passport.session());

passport.use(new GoogleStrategy({
    clientID: clientID,
    clientSecret: clientSecret,
    callbackURL: 'http://localhost:3000/auth/google/callback',
},
(accessToken, refreshToken, profile, done) => {
    return done(null, profile);
}));

passport.serializeUser((user, done) => {
    done(null, user);
});

passport.deserializeUser((user, done) => {
    done(null, user);
});

router.get('/auth/google', passport.authenticate('google', { scope: ['profile'] }));

router.get('/auth/google/callback',
    passport.authenticate('google', { failureRedirect: '/' }),
    (req, res) => {
        res.redirect('/profile'); // Redirect to profile route
    }
);

router.get('/profile', (req, res) => {
    res.json(req.user);
});

module.exports = router;
