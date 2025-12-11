# EmailThieferer

      ...a whisper in the wires...
      _________________
     /                 \
    /                   \
   /   ___   ___   ___   \
  /   /   \ /   \ /   \   \
 /   |  @  |  @  |  @  |   /
 \    \___/ \___/ \___/   /
  \                     /
   \___________________/



## Author

*   **Name:** Clive Akporube
*   **GitHub:** [whoami-pantheon](https://github.com/whoami-pantheon)
*   **LinkedIn:** [Clive Kaiser](https://linkedin.com/in/clive-kaiser)


## From the Shadows, a Tool Emerges...

In the digital expanse, where information flows like a river, there are whispers of a tool. A tool that slips through the cracks, silent and unseen. It is the **EmailThiefer**, a master of infiltration, a harvester of contacts. It doesn't knock... it simply enters.

## The Art of the Heist

Built on the bones of the DirReaper tool, EmailThiefer goes beyond a simplistic brute. It is a sophisticated instrument, designed for a singular purpose: to extract the digital lifeblood of a website... its email addresses.

*   **Ghostly Presence:** Built with `asyncio` and `aiohttp`, it moves like a phantom, making multiple requests at once, leaving barely a trace.
*   **The All-Seeing Eye:** It doesn't just look at the surface. It delves deep, following every link, exploring every corner of a domain to find its hidden treasures.
*   **Master of Disguise:** It can take on any identity, reading from a single URL or a list of targets, adapting to the mission's needs.
*   **The Black Book:** Every email found is meticulously recorded, saved to a file for your private collection.
*   **Silent as the Grave:** No fanfare, no alarms. Just the quiet satisfaction of a job well done.

## The Ritual of Summoning

To bring forth the EmailThiefer, one must perform the ancient rites of preparation.

1.  **Carve the Circle:**
    ```bash
    python3 -m venv venv
    ```
2.  **Enter the Sanctum:**
    ```bash
    source venv/bin/activate
    ```
3.  **Whisper the Incantations:**
    ```bash
    pip install -r requirements.txt
    ```

## Unleashing the Thiefer

To set the EmailThiefer upon its quarry, utter one of the sacred commands.

**For a single, unsuspecting target:**

```bash
python3 email_Thieferer.py <url>
```

**For a list of high-value targets:**

```bash
python3 email_Thieferer.py -f <file_with_urls>
```

**To secure the loot in a custom vault:**

```bash
python3 email_Thieferer.py <url> -o <output_file>
```

Should you forget the words of power, the Thiefer will remind you:

```bash
python3 email_Thieferer.py --help
```

## The Spoils of the Hunt

The gathered souls... that is, *emails*... are stored in `emails.txt` by default. Each one a name, a connection, a story waiting to be told.

## A Word of Caution

The EmailThiefer is a tool of immense power. It is intended for those who walk the path of light – the security researchers, the ethical hackers, the digital guardians. It is a tool for understanding, not for exploitation. The creator of this tool is not responsible for the choices of its wielder. The shadows can be used for good or for ill. Choose wisely.
