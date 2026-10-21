cd cse583/
mkdir pronto/
cd pronto/
touch README.txt
echo 'HW0 download and unzip files' > README.txt
mkdir data/
cd data/
curl -O https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
unzip open_data_year_one.zip
head 2015_trip_data.csv
