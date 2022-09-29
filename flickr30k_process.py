import argparse
import json
import os
from flickr30k_entities import flickr30k_entities_utils as f30k


def create_region_desc(sen_file, annot_file, image_id):
    sen_data = f30k.get_sentence_data(sen_file)
    anno_data = f30k.get_annotations(annot_file)

    image_info = {'id': int, 'regions': []}
    region_info = {'id': int, 'image_id': int, 'height': int, 'width': int, 'phrase': str, 'x': int, 'y': int}

    image_info['id'] = image_id
    for anno_id in anno_data['boxes'].keys():
        anno_boxes = anno_data['boxes'][anno_id]
        for anno_box in anno_boxes:
            for x in sen_data:
                for y in x['phrases']:
                    if y['phrase_id'] == str(anno_id):
                        region_info['id'] = int(y['phrase_id'])
                        region_info['image_id'] = image_id
                        region_info['height'] = anno_box[3]
                        region_info['width'] = anno_box[2]
                        region_info['phrase'] = y['phrase']
                        region_info['x'] = anno_box[0]
                        region_info['y'] = anno_box[1]
                        image_info['regions'].append(region_info.copy())

    return image_info


def main(args):
    flickr30k_regional_desc = []
    with open(args.splits_file, 'r') as f:
        splits = json.load(f)

    for key in splits:
        for image_id in splits[key]:
            sen_file = f'flickr30k_entities/Sentences/{image_id}.txt'
            annot_file = f'flickr30k_entities/Annotations/{image_id}.xml'
            flickr30k_regional_desc.append(create_region_desc(sen_file, annot_file, image_id))
            print(image_id, " done!")

    with open('flickr30k_regional_desc.json', 'w') as json_file:
        json.dump(flickr30k_regional_desc, json_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--splits_file', default='data/flickr30k_splits.json',
                        help='JSON file containing all the file names')

    args = parser.parse_args()
    main(args)
