const crypto = require('crypto');
const iv = "73a61538e3c11ded5603fee450686ef6";
const key = "002d088ecce426d47700930ba61668f65e77adf2ad298a1650e3a625eeb7c7db";
const cipher = crypto.createCipheriv('aes-256-cbc', Buffer.from(key, 'hex'), Buffer.from(iv, 'hex'));
let encryptedData = cipher.update("Hello bhai!", 'utf-8', 'hex') + cipher.final('hex')
console.log(encryptedData);
let decipher = crypto.createDecipheriv('aes-256-cbc', Buffer.from(key, 'hex'), Buffer.from(iv, 'hex'));
let decryptedData = (decipher.update(Buffer.from(encryptedData, 'hex')) + decipher.final()).toString()
console.log(decryptedData);