import glob
import json
import csv
import codecs

branch = 'training' # 'training' or 'validation'


# Set up output header and detail fields.
fields_h = ['filename', 'folder', 'imsize', 'scene']
fields_h_calc = ['header_id']
header_fields = fields_h_calc + fields_h
fields_d = ['id', 'raw_name', 'depth_ordering_rank', 'crop']
fields_d_calc = ['header_id', 'num_mask_points', 'xmin', 'ymin', 'xmax', 'ymax', 'size']
detail_fields = fields_d + fields_d_calc

# Fields from the files.
all_header_fields = ['filename', 'folder', 'imsize', 'source', 'scene']
all_detail_fields = ['id', 'name', 'name_ndx', 'hypernym', 'raw_name', 'attributes', 'depth_ordering_rank', 'occluded', 'crop', 'parts', 'instance_mask', 'polygon', 'saved_date']

# Prepare header and detail output files.
with open('ade20k_header.csv', 'w', newline='') as header_out, open('ade20k_detail.csv', 'w', newline='') as detail_out:
    writer_h = csv.DictWriter(header_out, fieldnames=header_fields)
    writer_h.writeheader()
    writer_d = csv.DictWriter(detail_out, fieldnames=detail_fields)
    writer_d.writeheader()

    # Go through each folder.
    for filename in sorted(glob.iglob('./images/ADE/{}/*/*/*.json'.format(branch), recursive=True)):

        print(filename)

        # Read the JSON file.
        with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as data_in:
            data = json.load(data_in)['annotation']

            # Write the header row.
            row_h = {}
            header_id = filename.split('_')[-1].split('.')[0]
            row_h['header_id'] = header_id
            for f in fields_h:
                row_h[f] = data[f]
            writer_h.writerow(row_h)

            # Write the detail row.
            for obj in data['object']:

                # Get the uncalculated fields.
                row_d = {k: obj[k] for k in fields_d} 

                # Get the header id.
                row_d['header_id'] = header_id

                # Get the number of mask points.
                poly = obj['polygon']
                row_d['num_mask_points'] = len(poly['x'])

                # Get min and max x and y.
                xmin = min(poly['x'])
                ymin = min(poly['y'])
                xmax= max(poly['x'])
                ymax= max(poly['y'])

                row_d['xmin'] = xmin
                row_d['ymin'] = ymin
                row_d['xmax'] = xmax
                row_d['ymax'] = ymax

                # Calculate size.
                row_d['size'] = (xmax-xmin) * (ymax-ymin)

                # Write detail row.
                writer_d.writerow(row_d)
