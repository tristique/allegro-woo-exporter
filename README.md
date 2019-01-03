Python scripts to easy move shops from Allegro to WooCommerce, by parsing allegro.pl web interface.

Input: seller's name, for example abc_pl

Output: CSV file ready to import to WooCommerce

Tasks:
- read shop's name
- enter to shop's profile and read number of pages with offers
- read and parse every page with 60 items (typically)
- enter every item and read parameters: title, description, number of pieces, price, photo's link etc.
- add item to CSV file and save file eventually.
