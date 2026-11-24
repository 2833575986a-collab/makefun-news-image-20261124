// news-image-20261124 entry (Node 22, standard library only): decodes the image drawn by draw.py and
// writes it to /output/entry.png. Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
import { writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { ENTRY_PNG_B64 } from './image.ts';

writeFileSync(join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'), Buffer.from(ENTRY_PNG_B64, 'base64'));
