train_test_split = { 
    'bcv_train': ['img0030', 'img0033',  'img0024', 'img0004', 'img0037', 'img0025', 'img0028', 'img0001', 'img0010', 'img0029', 'img0027', 'img0007', 'img0003', 'img0021', 'img0005', 'img0008', 'img0040', 'img0036', 'img0039', 'img0023', 'img0035', 'img0002', 'img0009'],
    'bcv_val': ['img0032'],
    'bcv_test': ['img0006', 'img0038', 'img0022', 'img0034', 'img0026', 'img0031'], 



    'amos_ct_train': [70, 56, 40, 117,  381, 387, 152, 35, 109, 64, 5, 66, 179, 330, 297, 161, 268, 147, 94, 7, 36, 156, 50, 60, 105, 177, 348, 294, 44, 14, 273, 378, 43, 67, 376, 133, 406, 188, 121, 390, 245, 336, 141, 115, 396, 230, 9, 320, 199, 311, 203, 356, 263, 337, 181, 21, 102, 23, 48, 391, 34,  27, 259, 180, 217, 196, 88, 276, 49, 321, 113, 71, 47, 225, 279, 41,  135, 349, 142, 403, 172, 125, 173, 237, 367, 281, 362, 248, 111, 17, 242, 30, 374, 45, 332, 341, 192, 272, 11, 153, 351, 58, 110, 317, 137, 408, 358, 138, 404, 42, 307, 57, 288, 143, 129, 160, 370, 118, 6, 119, 195, 184, 299, 214, 104, 69, 402, 10, 379, 134, 116, 400, 410, 19, 405, 282, 193, 15, 86, 16, 401, 170, 159, 239, 224, 383, 264, 81, 92, 38, 215, 274, 166, 4, 162, 249, 185, 392, 126, 154, 254, 371, 99, 76, 301, 235, 380, 124, 59, 84, 25, 171, 353, 24, 79, 398, 197, 33, 103, 77, 388, 1, 226, 83, 127, 231, 131, 186, 302, 361, 149, 89, 75, 384, 190], 
    'amos_ct_val': [212, 296, 366, 350, 98],
    'amos_ct_test': [13, 54, 292, 280, 29, 334, 257, 357, 326, 191, 238, 310, 373, 202, 247, 255, 228, 328, 363, 200, 78, 144, 290, 308, 208, 316, 216, 204, 304, 85, 189, 140, 158, 123, 286, 176, 284, 150, 395, 174, 206, 218, 318, 365, 377, 87, 372, 175, 198, 97, 339, 244, 344, 90, 293, 128, 155, 136, 63, 112, 52, 283, 157, 73, 61, 313, 325, 258, 409, 346, 106, 18, 22, 72, 287, 399, 333, 233, 250, 342, 309, 278, 223, 323, 194, 352, 364, 219, 207, 368, 8, 108, 167, 51, 132, 385, 32, 289, 397, 120], 



    'amos_mr_train': [553,  507, 571,576, 541, 538, 554, 597, 551, 558, 583, 600, 590, 508, 599, 572, 578, 584, 570, 544, 594, 557, 514, 595, 522, 582,  510, 530, 532, 596, 591, 592, 540, 580, 585, 517, 586, 589],
    'amos_mr_val': [518, 593],
    'amos_mr_test': [588, 575, 598, 559, 547, 563, 549, 545, 573, 561, 552, 568,  548, 550, 562, 546, 587, 556, 555, 581], 



    'structseg_oar_train': [5, 2,  7, 9, 10, 11, 12, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 45, 46, 47, 49, 50], 
    'structseg_oar_val': [3, 4],
    'structseg_oar_test': [44, 6, 29, 15, 37, 13, 1, 28, 48, 8], 

    'structseg_head_oar_train': [9, 3, 11, 4, 6, 7, 8, 43,  12, 13, 14, 15, 16, 17, 19, 20, 21, 23, 24,  26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 44,  46, 48, 49, 50],
    'structseg_head_oar_val': [25, 25],
    'structseg_head_oar_test': [1, 2, 45, 22, 47,  10, 5, 42, 40, 18],

    'lits_train': [ 6, 8, 10, 11, 12,  85, 14, 15, 4, 17, 19, 87,  21, 22,  2, 24,  27, 108, 29, 30, 31, 55, 34, 35, 36, 37, 38, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 5, 57, 58, 59, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 79, 80, 82, 83, 84, 86, 88, 89, 91, 92, 94, 95, 96, 97,  100, 101, 102, 103, 104, 105, 106, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 121, 123, 124, 125, 126, 128, 129, 130], 
    'lits_val': [0, 23, 3, 16, 98, 25],
    'lits_test': [1, 13, 7, 33, 127, 56, 118, 70, 26, 81, 78, 32, 20, 40,  122, 99, 71, 60, 42, 9, 28, 93, 39, 18, 77, 90],



    'kits_train': [0, 2, 3, 4, 5, 7, 8, 9, 11, 12,  23, 14, 15, 16, 20, 21,  24, 25, 27, 28, 30, 152, 33, 34, 35, 36,  38, 29, 41, 42, 39, 45, 47, 48, 185, 50, 52, 53,  56, 57, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69,  73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 90, 91, 94, 95, 96, 98, 99, 100, 101, 102, 103, 105, 106, 107, 109,  111, 112, 113, 114, 115, 116, 117, 119, 120, 121, 122, 123, 124, 125, 126,  128, 129, 130, 132, 133, 135, 136, 137, 138, 139, 140, 141, 142, 143, 145, 147, 148, 149, 150, 151, 153, 154, 155, 156, 157, 158, 160, 162, 163, 164, 166, 168, 169, 171, 172, 173, 174, 175, 176, 177,  180, 182, 183, 186, 187,189, 190, 191, 192, 194, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209],
    'kits_val': [1, 161, 18, 37, 55, 110, 127,89, 40],
    'kits_test': [43,  196, 10, 159, 46, 184, 13, 19, 195, 144, 17, 188, 51, 170, 58, 26, 193, 44, 165, 134, 118, 104, 31, 32, 71, 179,  93, 72, 97, 70, 54, 22, 167, 92, 108, 181, 146, 6, 131, 76, 49, 178],



    'chaos_train': ['20', '1', '38', '3', '34', '8', '10', '2', '13', '37', '39', '15', '21', '33', '19'], 
    'chaos_val': ['22'],
    'chaos_test': ['31', '5', '32', '36'],

    'mnm_train': ['A4B5U4', 'A4J4S4', 'A4U9V5', 'A6D5F9',  'G7I5V7', 'E5F5V7', 'B2G5R2', 'H5N0P0', 'G2O2S6', 'J1T9Y1', 'G8N2U5', 'I6N3P3', 'G0H4J3', 'E0O0S0', 'G4L8Z7', 'Q7V1Y5', 'E3T0Z2', 'F3G5K5', 'F1F3I6', 'N7V9W9', 'N8N9U0', 'G2M7W4', 'I2K2Y8', 'H1J5W8', 'K2S1U6', 'J4J9W6', 'J6P5T8', 'K4T7Y0', 'I0J5U3', 'H6I0I6',  'A9J8W7', 'B3O1S0', 'B2D9M2', 'D3F9H9', 'B3P3R1', 'D6H6O2', 'B9O1Q0', 'E4M2Q7', 'C2L5P7', 'A0S9V9', 'D8E4F4', 'J6K6P5', 'L1Q1Z5', 'I7T3U1', 'O0S9V7', 'A7D9L8', 'A6M1Q7', 'F8N2S1', 'K5P0Y1', 'B2C2Z7',  'G4S9U3', 'K5L2U3', 'P0S5Y0', 'P5R1Y4', 'P6U0Y0', 'P9S7W2', 'Q0U0V5', 'Q3R9W7', 'R4Y1Z9', 'S1S3Z7', 'D4N6W6', 'F4K3S1', 'F5I9Q2', 'F0J2R8', 'G1N6S7', 'H1M5Y6', 'F2H5S1', 'H0K3Q4', 'G0I6P3', 'A1D0Q7', 'E5E6O8', 'A1D9Z7', 'A1E9Q1', 'A9J5Q7', 'D1L4Q9', 'C2M6P8', 'C1K8P5', 'B2F4K5', 'B2D9O2', 'C2J0K3', 'C1G5Q0', 'B3D0N1', 'B6D0U7', 'B4O3V3', 'C5M4S2', 'B8J7R4', 'C4R8T7', 'C0S7W0', 'C0K1P0', 'E9H1U4', 'E9L1W5', 'D3O9U9', 'D1M1S6', 'E0M3U7', 'G9L0O9', 'H4I2T8', 'H1W2Y1', 'G5P4U3', 'H3U1Y1', 'J8R5W2', 'O3R8Y5', 'E9H2K7', 'J9L6N9', 'L4Q2U3', 'L1Q9V8', 'M0P8U8', 'M1R4S1', 'M2P1R1', 'M4P7Q6', 'N1P8Q9', 'N5S7Y1', 'D9L1Z3', 'E9V4Z8', 'H7N4V9', 'T2T9Z9', 'T9U9W2', 'W5Z4Z8', 'A6B5G9', 'H1I3W0', 'E4W8Z7', 'D0R0R9', 'A5E0T8', 'C3I2K3', 'C8P3S7', 'D4M3Q2', 'A1O8Z3', 'A8E1F4', 'A7M7P8', 'A2C0I1', 'A2N8V0', 'A3B7E5', 'A3H1O5', 'D0H9I4', 'D3D4Y5', 'C4S8W9', 'D3F3O5', 'D1J5P6', 'A7G0P5', 'A9E3G9',  'A7O4T6', 'A8C9U8', 'B9E0Q1', 'B0N3W8'],
    'mnm_val': ['G2J1M5', 'H7I4J3', 'L5Q6T7', 'A9C5P4', 'B8H5H6', 'B0I2Z0', 'C6J5P1'],
    'mnm_test': ['K3R0Y7', 'K5M7V5', 'E4O8P3', 'E1L8Y4', 'O7Q7U3', 'D2U0V0', 'P8V0Y7', 'D8O0W2', 'C8I7P7', 'C5L0R0', 'C8J7L5', 'H3R6S9', 'K5K6N1', 'E3F2U7', 'J6M5O2', 'F6J9L9', 'D1R0Y5', 'C6E0F9', 'A9F3T5', 'H6P7T1', 'D7T3V8', 'A5C2D2', 'D5G3W8', 'D1H6U2', 'C4E9I1', 'D1S5T8', 'N2O7U5', 'G7Q2W0', 'I7W4Y8', 'B0H7V0', 'K9N0W0', 'D7M8P9', 'D6N7Q8', 'I4L4V7', 'A4B9O6', 'B5F8L9', 'K6N4N7', 'A5H1Q2', 'A5Q1W8', 'M6M9N1', 'M6V2Y0', 'R1R6Y8', 'R3V5W7', 'D3Q0W9', 'D9F5P1', 'C6U4W8', 'K7L2Y6', 'L7Y7Z2', 'B5L5Y4', 'B6I0T4', 'G8K0M3', 'B0L3Y2', 'J6K4V3', 'J9L4S2', 'K7O3Q0', 'Q4W5Z8', 'A7F4G2', 'B9H8N8', 'C8O0P2', 'E5S7W7', 'H7P5Z4', 'B1G9J3', 'E1L7M3', 'K3P3Y6', 'K5L4S1', 'A8C5E9', 'F0I6U8', 'F0K4T6', 'F5I1Z8', 'G1K1V3', 'F1K2S9', 'I8N8Y1', 'B9G4U2', 'I6P4R0', 'A2L1N6', 'B2L0L2', 'B4S1Y2', 'G8L0Z0', 'I8Z0Z6', 'J4J8Q3', 'A3P9V7', 'A6J0Y2', 'B3E2W8', 'D6E9U8', 'L8M2U8', 'L8N7P0', 'L8N7Z0', 'M2P5T8', 'M4T4V6', 'Q5V8W3', 'A5P5W0', 'Y6Y9Z2', 'B3S2Z4', 'B4E1K1', 'B3F0V9', 'B7F5P0', 'C7L8Z8', 'C7M6W0', 'D1H2O9', 'E6J4N8', 'O4O6U5', 'A1K2P5', 'G4I7V2', 'I2J6Z6', 'I5L3S2', 'I4R8V6', 'E7L0N6', 'E9V9Z2', 'G3M5S4', 'H1N8S6', 'T2Z1Z9', 'R8V0Y4', 'V4W8Z5', 'D3K5Q2', 'D9I8O7', 'E6M6P2', 'I0I2J8', 'K7N0R7', 'O9V8W5', 'P3T5U1', 'A7E4J0', 'B8P5Q9', 'C0N8P4', 'D1L6T4', 'O4T6Y7', 'A4R4T0', 'A4A8V9', 'A6B7Y4', 'C0L7V1', 'F9M1R2', 'E4H7L4', 'L5U7Y4', 'A9L7Y7', 'N7W6Z8', 'N7P3T8', 'A2H5K9', 'A6A8H0', 'G1J5K3', 'N9P5Z0', 'N9Q4T8', 'P3P9S5', 'P3R6Y5', 'B5T6V0', 'E6H0V9', 'H7K5U5', 'L6T2T5', 'Q1Q3T1', 'O5U2U7', 'P8W4Z0', 'Q3Q6R8', 'R2R7Z5', 'R6V5W3', 'A3H5R1', 'A4K8R4', 'A5D0G0', 'G8R0Z9', 'E3F5U2', 'E3L8U8', 'G7S6V0', 'I6T4W8', 'H2M9S1', 'H7L8R8', 'H8K2K7', 'E0J2Z9', 'E4I9O7', 'L2V5Z0', 'E0J7L9', 'E5J6L2', 'G7N8R7', 'G9N5V9'],
    
    'autopet_train': ['PETCT_0011f3deaf_0','PETCT_0117d7f11f_0','PETCT_0143bab87a_0','PETCT_01682f60c3_0','PETCT_0168f65af8_0','PETCT_0223010e46_0','PETCT_0225325b91_0','PETCT_02ba7e20f5_0','PETCT_0410759456_0','PETCT_0410759456_1','PETCT_04606080a0_0','PETCT_048981112f_0','PETCT_04a4e1c874_0','PETCT_05bed31780_0','PETCT_05d5a79faf_0','PETCT_05d8640f52_0','PETCT_06a46414eb_0','PETCT_06d55e8295_0','PETCT_06e7c24059_0','PETCT_072833774e_0','PETCT_07574bfa00_0','PETCT_07fec0d985_0','PETCT_080922db5a_0','PETCT_08198c4f0c_0','PETCT_08212d7f6c_0','PETCT_08cdb15e0b_0','PETCT_098c4b7b87_0','PETCT_099b3fd402_0','PETCT_0af7ffe12a_0','PETCT_85b69fed1c_0','PETCT_68f73c4518_0','PETCT_38a374d01a_0','PETCT_527c5afc5d_0','PETCT_9ffd8409b3_0','PETCT_9f491f1481_0','PETCT_cf20ad1656_0','PETCT_68b75093c5_0','PETCT_9f6e8b1b43_0','PETCT_cf3725edf0_0','PETCT_68ef307665_0','PETCT_9f7c68f5ca_0','PETCT_5a58935b68_0','PETCT_ae96f738c0_0','PETCT_ae96f738c0_1','PETCT_5ac322455f_0','PETCT_c2ffda4725_0','PETCT_c2ffda4725_1','PETCT_4481687483_0','PETCT_84e7715ed9_0','PETCT_448225c237_0','PETCT_855c7fca12_0','PETCT_86153b2974_0','PETCT_86153b2974_1','PETCT_86153b2974_2','PETCT_86153b2974_3','PETCT_86153b2974_4','PETCT_c395306306_0','PETCT_c3cc732d95_0','PETCT_44bf7dc508_0','PETCT_44c04dcf65_0','PETCT_44cfacfd6e_0','PETCT_c517c47bed_0','PETCT_86e54ea60a_0','PETCT_c58477f3b4_0','PETCT_44d6ba6772_0','PETCT_c58b637e17_0','PETCT_870181d7fd_0','PETCT_c596a50286_0','PETCT_465176d213_0','PETCT_46ee4ddd68_0','PETCT_c5a143a604_0','PETCT_87afc291ec_0','PETCT_87afc291ec_1','PETCT_c6730783de_0','PETCT_4776e75543_0','PETCT_8838c53a63_0','PETCT_88bcc970b3_0','PETCT_4785066413_0','PETCT_47cd731006_0','PETCT_89065bc4ab_0','PETCT_c7fd7e3e30_0','PETCT_89fb723947_0','PETCT_47f4460050_0','PETCT_c852dfc0a5_0','PETCT_c898e2abcb_0',
'PETCT_4848bebb10_0','PETCT_48a34ccdf0_0','PETCT_48c70dc4a3_0','PETCT_48c70dc4a3_1','PETCT_c9f1b9980f_0','PETCT_8af3757198_0','PETCT_8b14e6a819_0','PETCT_8b40e356dc_0','PETCT_ca29501275_0','PETCT_48d5467561_0','PETCT_48d5467561_1','PETCT_ca47fe5e7d_0','PETCT_8b714a64e7_0','PETCT_8b74860ce6_0','PETCT_ca5406d339_0','PETCT_49479d6e64_0','PETCT_ca58410fad_0','PETCT_49f3d297b0_0','PETCT_ca62984a81_0','PETCT_8bf08c9a42_0','PETCT_ca89066e44_0','PETCT_8c5d99b459_0','PETCT_4a0d2e5166_0','PETCT_ca9570a0eb_0','PETCT_4a255db7bd_0','PETCT_8c8cd2699c_0','PETCT_8de6953d23_0','PETCT_4b688f46b0_0','PETCT_4bab91dccd_0','PETCT_cb1f5e74ab_0','PETCT_8de70b5cd7_0','PETCT_4c670a5445_0','PETCT_cb83710e3d_0','PETCT_8e905366fe_0','PETCT_cbbc9e2879_0','PETCT_cbbc9e2879_1','PETCT_cbbc9e2879_2','PETCT_cbbc9e2879_3','PETCT_8eb3998417_0','PETCT_8ec13728df_0','PETCT_4c75fa4a5d_0','PETCT_8f2878df50_0','PETCT_8f2878df50_1','PETCT_4c9e7be363_0','PETCT_8fea5f0537_0','PETCT_4cb875dc0b_0','PETCT_cc5c58c82d_0','PETCT_901573a747_0','PETCT_cc7cb73213_0','PETCT_90d668ed29_0','PETCT_ccb9c375b2_0','PETCT_4cc808d16f_0','PETCT_cd2ef932b5_0','PETCT_912a25778f_0','PETCT_91cfa804b0_0','PETCT_cd50f3fec4_0','PETCT_4d7b745a7b_0','PETCT_92c3de23f5_0','PETCT_0b57b247b6_0','PETCT_cd9bdca46b_0','PETCT_4dcf62f869_0','PETCT_92c5c944a5_0','PETCT_0b98dbe00d_0','PETCT_4ea806706c_0','PETCT_93bea242d1_0','PETCT_4ef69de4e1_0','PETCT_0cda25453b_0','PETCT_94962fe878_0','PETCT_4f6ff86453_0','PETCT_94986389d4_0','PETCT_4f7a8f41c0_0','PETCT_94cc0dac49_0','PETCT_94cc0dac49_1','PETCT_0dbf2c2731_0','PETCT_4fb1817df3_0','PETCT_0e2034240b_0','PETCT_5001354a69_0','PETCT_d098458d29_0','PETCT_5060603ba4_0','PETCT_9521502dbb_0','PETCT_0ea07b421b_0','PETCT_5109748328_0','PETCT_956520090b_0','PETCT_0f44cec2e6_0','PETCT_510fb36781_0','PETCT_95efdaba3c_0','PETCT_d103e57f0e_0','PETCT_5255c79083_0','PETCT_d1c8141930_0','PETCT_0fa313309d_0','PETCT_0fa313309d_1','PETCT_d206b891ee_0','PETCT_53a0610615_0','PETCT_d27451634d_0','PETCT_963a71819a_0','PETCT_1019ae8551_0','PETCT_108c1763d4_0','PETCT_d31a5688a2_0','PETCT_96e7a3ab28_0','PETCT_d31c9ebd93_0','PETCT_119165872d_0','PETCT_d3208ff062_0','PETCT_978c395243_0','PETCT_d32cf972af_0','PETCT_12025abab5_0','PETCT_979f9c3dba_0','PETCT_1253499c80_0','PETCT_9837205b34_0','PETCT_983a76fd43_0','PETCT_1285b86bea_0','PETCT_d3d3b7d4ff_0','PETCT_1291700093_0','PETCT_9860ffe82d_0','PETCT_d3d61785e6_0','PETCT_13b40a817b_0','PETCT_987c8a1160_0','PETCT_98c6af8b90_0','PETCT_98cd91d44e_0','PETCT_d3f13dff4b_0','PETCT_13f476b02b_0','PETCT_9902caa7ec_0','PETCT_d40a16781a_0','PETCT_993d40ea7e_0','PETCT_d4112bc7ba_0','PETCT_997d4ef9a7_0','PETCT_141fffa2a9_0','PETCT_99a7bfad23_0','PETCT_1472967bef_0','PETCT_99e5728030_0','PETCT_d4a08e4bde_0','PETCT_9a2bfe901f_0','PETCT_d4b2ff9721_0','PETCT_14929994cf_0','PETCT_14c4d2c208_0','PETCT_14f931f634_0','PETCT_d4f3375362_0','PETCT_9a583160ea_0','PETCT_d51664a9e4_0','PETCT_1553bd8c8f_0','PETCT_d51bacdaba_0',
'PETCT_15cfa01130_0','PETCT_d539f5a88b_0','PETCT_15f4b7254f_0','PETCT_15f4b7254f_1','PETCT_9a83943958_0','PETCT_d626611daf_0','PETCT_d626611daf_1','PETCT_d626611daf_2','PETCT_d626611daf_3','PETCT_d626611daf_4','PETCT_9abb9583ec_0','PETCT_9ad7dffae6_0','PETCT_173b804eda_0','PETCT_9afd440677_0','PETCT_176bdc5388_0','PETCT_9b1bb2165a_0','PETCT_1781ba966c_0','PETCT_9b982e72cb_0','PETCT_17b46d7275_0','PETCT_d64d6a87c8_0','PETCT_17d334cb6c_0','PETCT_9c68e484a7_0','PETCT_d674a028b1_0','PETCT_182bdeba22_0','PETCT_185bac7954_0','PETCT_9c8842d12e_0','PETCT_18e8b02af3_0','PETCT_9c9a347388_0','PETCT_1928952a0f_0','PETCT_9d6699f215_0','PETCT_9d6e9223cc_0','PETCT_193dea6ac7_0','PETCT_9d97ac5d4d_0','PETCT_1956667fce_0','PETCT_1956667fce_1','PETCT_9da159b835_0','PETCT_d6a491e16d_0','PETCT_19838cb8e5_0','PETCT_19b68a666b_0','PETCT_d6b2218bf3_0','PETCT_9e864bb710_0','PETCT_d6de1252d9_0','PETCT_9f206193d3_0','PETCT_9f206193d3_1','PETCT_d8d9e52cd5_0','PETCT_d8d9e52cd5_1','PETCT_d8d9e52cd5_2','PETCT_d8d9e52cd5_3','PETCT_1a3d4e63ee_0','PETCT_1a8bd52f71_0','PETCT_1a90052cb2_0','PETCT_1a90052cb2_1','PETCT_a09210d96b_0','PETCT_1ac497ed9d_0','PETCT_1b199d094d_0','PETCT_a0c4dc1ef1_0','PETCT_1b1bdfc35b_0','PETCT_1bb48bfb40_0','PETCT_d8e3aa97a0_0','PETCT_d951eeb735_0','PETCT_d9da6129f8_0','PETCT_a1d93ebc74_0','PETCT_da4ce0da01_0','PETCT_1cb2d26a19_0','PETCT_a1db71e797_0','PETCT_da6161d7eb_0','PETCT_1e43e3d692_0','PETCT_a21200dcba_0','PETCT_dac5cd2a4d_0','PETCT_a22ec7f62b_0','PETCT_1f2a4f4280_0','PETCT_1f2a4f4280_1','PETCT_a25083ff81_0','PETCT_1f65acff65_0','PETCT_a2676f03c0_0','PETCT_dae86b88e2_0','PETCT_db3bac356a_0','PETCT_a29cae0316_0','PETCT_1f6b6b0548_0','PETCT_a2a68bbe97_0','PETCT_a37b4bca43_0','PETCT_1fa22c576e_0','PETCT_dc15c1d9bb_0','PETCT_a37c4e231f_0','PETCT_dc3437c9b9_0','PETCT_a37da9e85d_0','PETCT_dc6174cb5d_0','PETCT_dc6174cb5d_1','PETCT_a3ce52b2a8_0','PETCT_a3ce52b2a8_1','PETCT_1fcfa34d10_0','PETCT_1fe6e48293_0','PETCT_a3df01d3a3_0','PETCT_dd6165ae36_0','PETCT_a41d59682f_0','PETCT_dd68a71e0a_0','PETCT_20995a0fe1_0','PETCT_a471649d35_0','PETCT_a4a66c4fa7_0','PETCT_a4cb97ffc7_0','PETCT_dd8f9f217c_0','PETCT_20f4a3aa02_0','PETCT_a4ccc397a9_0','PETCT_2122b88719_0','PETCT_a4cd2b10de_0','PETCT_a4cd2b10de_1','PETCT_a4cd2b10de_2','PETCT_21853fc15b_0','PETCT_21e4ffcb52_0','PETCT_ddbb3c69f0_0','PETCT_a4ff5d0d9d_0','PETCT_223f70f0b0_0','PETCT_ddca6cfba6_0','PETCT_22d07bdc49_0','PETCT_a57bd6b006_0','PETCT_de118d7ab9_0','PETCT_dec9ff6a91_0','PETCT_ded50b1e68_0','PETCT_a627fc68a1_0','PETCT_df2e16771a_0','PETCT_245182006a_0','PETCT_e00c98b415_0','PETCT_e03b96666f_0','PETCT_249c02c01c_0','PETCT_249c02c01c_1','PETCT_a82f03863a_0','PETCT_e04b7fa860_0','PETCT_a86b2dc6ce_0','PETCT_e09a20d8fc_0','PETCT_e0a7ccecad_0','PETCT_a86b3fad40_0','PETCT_249dd35d0c_0','PETCT_e0aa99fa04_0','PETCT_24cb79a92b_0','PETCT_e0fdc6212a_0','PETCT_a87dda9193_0','PETCT_e1a4145b63_0','PETCT_a8a5e96821_0','PETCT_a8a5e96821_1','PETCT_e1a5b05186_0',
'PETCT_e207c7a1a4_0','PETCT_e2309b8f92_0','PETCT_a933c9af60_0','PETCT_e252be4334_0','PETCT_e2834e6f5c_0','PETCT_a9d7a14ba1_0','PETCT_aa27cb9156_0','PETCT_2745fb1adb_0','PETCT_274688d0a8_0','PETCT_e37d5b9bc2_0','PETCT_e44480b9b8_0','PETCT_277fc3c67c_0','PETCT_e4749cda88_0','PETCT_27d69a8466_0','PETCT_28a0a0a163_0','PETCT_e4e5baf901_0','PETCT_2922971d0f_0','PETCT_e4e99dbb47_0','PETCT_2946d59a94_0','PETCT_e52eca67d7_0','PETCT_e5c7be07a8_0','PETCT_29b372cb99_0','PETCT_e5d50c5569_0','PETCT_2a6f4f0753_0','PETCT_e5e1918765_0','PETCT_2a78eed085_0','PETCT_e664932bbc_0','PETCT_e68c4577d8_0','PETCT_2ad62beb52_0','PETCT_2b29531d8c_0','PETCT_2b60c8135a_0','PETCT_e6a91fef70_0','PETCT_e6b8b963b2_0','PETCT_2b8064fbe2_0','PETCT_e77c5fca12_0','PETCT_e79291780d_0','PETCT_2d70838805_0','PETCT_e8624bab41_0','PETCT_2d9638360e_0','PETCT_2dac5ef654_0','PETCT_e90a287d09_0','PETCT_e90a287d09_1','PETCT_e9be8ec30f_0','PETCT_e9e1a391b5_0','PETCT_2e97a9e5c2_0','PETCT_e9feb1135e_0','PETCT_e9feb1135e_1','PETCT_2f2ee78c89_0','PETCT_ea051a3e6c_0','PETCT_ea0fd89f0f_0','PETCT_ea42c88cc7_0','PETCT_2f9aec0275_0','PETCT_2f9aec0275_1','PETCT_30001118d0_0','PETCT_eafa147e24_0','PETCT_ebb0045704_0','PETCT_30287f520f_0','PETCT_ec581d49ef_0','PETCT_ec581d49ef_1','PETCT_3049d4f1a4_0','PETCT_ec6b934720_0','PETCT_30c4b7062b_0','PETCT_ed7abf4433_0','PETCT_ed9dca00d2_0','PETCT_30e2b83b74_0','PETCT_30e2b83b74_1','PETCT_30e2b83b74_2','PETCT_ed9fa4eff1_0','PETCT_eda00de6b0_0','PETCT_31ddf5013a_0','PETCT_ee97822c60_0','PETCT_eee2ede9ad_0','PETCT_eeeda112bb_0','PETCT_321bba14bc_0','PETCT_32219760da_0','PETCT_323cc5aff8_0','PETCT_f01e83894d_0','PETCT_f068e22258_0','PETCT_f082a3d319_0','PETCT_f0a1a38a3b_0','PETCT_f0e1b89b41_0','PETCT_34aa521b46_0','PETCT_34d3efa936_0','PETCT_f1594a7d8a_0','PETCT_36870de2f2_0','PETCT_f21755a99b_0','PETCT_36bb0257fc_0','PETCT_3708f576ec_0','PETCT_f2f28337ba_0','PETCT_372746cc99_0','PETCT_f4668d2bdc_0','PETCT_37472e737f_0','PETCT_37952b7ffb_0','PETCT_38733c001e_0','PETCT_389462c0ac_0','PETCT_389462c0ac_1','PETCT_389462c0ac_2','PETCT_f4813007a0_0','PETCT_f5c9b0de6c_0','PETCT_f5cff2e59d_0','PETCT_390129c0d2_0','PETCT_f637b5930b_0','PETCT_39159c05c2_0','PETCT_f650c87621_0','PETCT_f650c87621_1','PETCT_3a40a26443_0','PETCT_f65602d938_0','PETCT_3a4be713a1_0','PETCT_3b14690fce_0','PETCT_3b1c9155f5_0','PETCT_3b26172779_0','PETCT_3b73c2480a_0','PETCT_f8314eb3f7_0','PETCT_f8314eb3f7_1','PETCT_3ba0277c0c_0','PETCT_f8aac0e202_0','PETCT_f8aac0e202_1','PETCT_3bce0eb7aa_0','PETCT_3c3050f75e_0','PETCT_3c3ee87fc6_0','PETCT_f8de0cde56_0','PETCT_f9c4d4f9ab_0','PETCT_3c71e8f518_0','PETCT_3c94a00f90_0','PETCT_f9e0c504af_0','PETCT_3cd49210eb_0','PETCT_fa45f610c4_0','PETCT_3d6f425a76_0','PETCT_3d6f425a76_1','PETCT_fb014a1ea0_0','PETCT_3eac8f16d4_0','PETCT_fbd907a179_0','PETCT_fc0389a486_0',
'PETCT_40f0749cb7_0','PETCT_416d3b9b78_0','PETCT_41bd54f97a_0','PETCT_ff1451316e_0','PETCT_41f4d41517_0','PETCT_ff39795341_0','PETCT_41fadf6520_0','PETCT_424e9b79c5_0','PETCT_4250de48c8_0','PETCT_42e9f16c09_0','PETCT_43323b7d42_0','PETCT_43647ff727_0','PETCT_43c9c71b31_0','PETCT_c29aba73da_0','PETCT_c252d734a0_0','PETCT_82137245b0_0','PETCT_c1c9e78e0e_0','PETCT_81debf13a1_0','PETCT_816732638d_0','PETCT_c16c13211c_0','PETCT_c10f48b173_0','PETCT_80f7760f65_0','PETCT_80f7760f65_1','PETCT_c094a24c03_0','PETCT_c094a24c03_1','PETCT_c08293f2b2_0','PETCT_c018b45a49_0','PETCT_80d7e682f7_0','PETCT_bfd89440db_0','PETCT_bfd89440db_1','PETCT_80ccbdadf9_0','PETCT_bf7652bccc_0','PETCT_80b8393c44_0','PETCT_bf178a41b2_0','PETCT_802f19931c_0','PETCT_bef465b4ad_0','PETCT_be3e55a32f_0','PETCT_be0d3c767e_0','PETCT_7f2a604e03_0','PETCT_bdd21f5590_0','PETCT_7ef5343426_0','PETCT_bd7c02faa9_0','PETCT_7ee7610b9e_0','PETCT_bd76c8d299_0','PETCT_7ed037687a_0','PETCT_7e5729ea40_0','PETCT_bd52fdf529_0','PETCT_7e56b0b62c_0','PETCT_7d97f7a102_0','PETCT_bca97006e4_0','PETCT_7d8aa1e94d_0','PETCT_bc80d06f97_0','PETCT_bbb83facb4_0','PETCT_7cfd708a53_0','PETCT_bbb2df1e31_0','PETCT_bb564e29d2_0','PETCT_7cfaf65584_0','PETCT_7ce196485f_0','PETCT_baacf43b4f_0','PETCT_ba81e4b04b_0','PETCT_7c96c4626d_0','PETCT_ba717a1f22_0','PETCT_7c1e6175e0_0','PETCT_b92d7f441e_0','PETCT_b926177c87_0','PETCT_7b9d625330_0','PETCT_b899150306_0','PETCT_7b477e7e0d_0','PETCT_7b477e7e0d_1','PETCT_b7c1533a39_0','PETCT_7b42056ee3_0','PETCT_b79961f3f6_0','PETCT_7abe274c10_0','PETCT_b6fc20942c_0','PETCT_7a8a062ed5_0','PETCT_7a77b26403_0','PETCT_b6a3c72db6_0','PETCT_7a3a27371a_0','PETCT_b6a1ee33ef_0','PETCT_7a262070a9_0','PETCT_b66ba83594_0','PETCT_1a1712f7d0_0','PETCT_1a1712f7d0_1','PETCT_1a1712f7d0_2','PETCT_d7ca3d4aaa_0','PETCT_d8a92bafe3_0','PETCT_a19ef8e0d2_0','PETCT_7978e9fe62_0','PETCT_b663adb148_0','PETCT_1fc35d02da_0','PETCT_792d7b6ad0_0','PETCT_791ec15924_0','PETCT_790246c76c_0','PETCT_78b89bc739_0','PETCT_b57e1c1f5f_0','PETCT_78355d1d4f_0','PETCT_b53ba7c6bf_0','PETCT_b52920038c_0','PETCT_b509ace2a2_0','PETCT_770ee48d09_0','PETCT_b4e5c1047c_0','PETCT_b42adab18e_0','PETCT_75e42ff05f_0','PETCT_75210090cd_0','PETCT_b3d4773f85_0','PETCT_75046e0c12_0','PETCT_74bbceaeeb_0','PETCT_b327726c24_0','PETCT_742a9413db_0','PETCT_b258dfa7c2_0','PETCT_73fda3a382_0','PETCT_7365362464_0','PETCT_b1aa7ce13e_0','PETCT_73597f33fe_0','PETCT_73597f33fe_1','PETCT_b1219c408b_0','PETCT_b0e002e974_0','PETCT_b0e002e974_1','PETCT_b0e002e974_2','PETCT_72ee9ec897_0','PETCT_b04be2846e_0','PETCT_7255ccbcf4_0','PETCT_71ae114917_0','PETCT_af547fa618_0','PETCT_af119148fe_0','PETCT_af119148fe_1','PETCT_af119148fe_2','PETCT_71ac560ffe_0','PETCT_7094acd4c0_0','PETCT_aee7d68f86_0','PETCT_aea7906fd2_0','PETCT_6f46454a8d_0','PETCT_6f46454a8d_1','PETCT_6f46454a8d_2','PETCT_ae8c77a995_0',
'PETCT_ac700ab4db_0','PETCT_6aea5c3a03_0','PETCT_ac11b344b6_0','PETCT_ab953a5230_0','PETCT_6a3477cd9a_0','PETCT_69ee62b035_0','PETCT_69aa8dbfd2_0','PETCT_685d7c09b5_0','PETCT_674c49778c_0','PETCT_661ddc60e0_0','PETCT_6604b228c6_0','PETCT_65a1330e90_0','PETCT_6543c58e13_0','PETCT_64c0cba177_0','PETCT_64aff75516_0','PETCT_64aff75516_1','PETCT_64909533c5_0','PETCT_644d80e987_0','PETCT_63508c679d_0','PETCT_63508c679d_1','PETCT_631b419cef_0','PETCT_62ced197ca_0','PETCT_62a78a061f_0','PETCT_62011ff15b_0','PETCT_6170317f2e_0','PETCT_61348439bf_0','PETCT_60baa6979c_0','PETCT_6016a6c3af_0','PETCT_5fa9d9a820_0','PETCT_5fa9d9a820_1','PETCT_5fa9d9a820_2','PETCT_5fa9d9a820_3','PETCT_5f569fb737_0','PETCT_5ef99b0b6b_0','PETCT_8e02f36295_0','PETCT_5e81863014_0','PETCT_5e339b2ecf_0','PETCT_5e339b2ecf_1','PETCT_5e339b2ecf_2','PETCT_5e0bc6cdda_0','PETCT_5de3ac617a_0','PETCT_5d994c3f44_0','PETCT_5d6bf1e75f_0','PETCT_5cf118ac06_0','PETCT_5c55b3087d_0','PETCT_5c35fcbe89_0', 'PETCT_0f4ee9e078_0', 'PETCT_5bd311a5e9_0','PETCT_5b0aa4e971_0','PETCT_5a274a0f26_0','PETCT_11afab3485_0','PETCT_595975bc57_0','PETCT_59309d6625_0','PETCT_591b3025ff_0','PETCT_58f276897e_0','PETCT_57c05962c1_0','PETCT_572fca6b44_0','PETCT_d3dac0d1cd_0','PETCT_55d55902c6_0','PETCT_55ca11402a_0','PETCT_55819a54c2_0','PETCT_556b56485a_0','PETCT_548213edf7_0','PETCT_544676de40_0','PETCT_544676de40_1','PETCT_544676de40_2','PETCT_5420205a5f_0','PETCT_53dad1785b_0','PETCT_53ccb9efbb_0','PETCT_846c1af245_0','PETCT_83e4c5b578_0','PETCT_c2a51a65c6_0'],
    'autopet_val': [ 'PETCT_8aa48809ea_0', 'PETCT_456d14846b_0', 'PETCT_b5923963ac_0', 'PETCT_fcdbe15200_0', 'PETCT_402c061122_0','PETCT_402c061122_1', 'PETCT_44b08f570e_0', 'PETCT_404f8c732f_0','PETCT_4095c12e2d_0','PETCT_40a125468a_0','PETCT_6e7c7f8087_0','PETCT_6dd36a2c19_0','PETCT_ae4dcc5dd3_0','PETCT_ae46202abb_0','PETCT_ae3074834a_0', 'PETCT_01140d52d8_0', 'PETCT_04ab5c61c9_0', 'PETCT_6c23f2686d_0', 'PETCT_97320b0b58_0','PETCT_97320b0b58_1', 'PETCT_6b20c7eabb_0'],
    'autopet_test':['PETCT_36d8219e3f_0','PETCT_f47e31ceb5_0','PETCT_380f71df1e_0','PETCT_38106fde84_0','PETCT_f4a5ebd915_0','PETCT_f6295a93a6_0', 'PETCT_fde66dd53a_0', 'PETCT_ad7cd4a9d2_0', 'PETCT_05808cf24e_0','PETCT_05808cf24e_1','PETCT_09ee00bdc6_0','PETCT_d0ea6c975f_0','PETCT_4011ffe8ae_0', 'PETCT_b5923963ac_1','PETCT_389c968170_0','PETCT_389c968170_1','PETCT_6c660140ca_0', 'PETCT_c38b168f1a_0','PETCT_44b95650c3_0','PETCT_c4a686881e_0','PETCT_3fd361ec14_0', 'PETCT_456e6f9dc2_0','PETCT_474d7af918_0','PETCT_4760c0139a_0','PETCT_c73c2685c0_0','PETCT_c787334539_0','PETCT_c799ccc2f6_0','PETCT_c7dc6f848c_0', 'PETCT_3f3df20439_0','PETCT_48cb8662f7_0','PETCT_ca16242e89_0','PETCT_ca16242e89_1','PETCT_8b73608326_0','PETCT_8bebb676bf_0','PETCT_caae8d63f0_0','PETCT_4a72eeb991_0','PETCT_cab58c1fee_0','PETCT_4be28f9cd7_0','PETCT_cb240e6f0f_0', 'PETCT_5e8b013935_0', 'PETCT_90ea6a6aaf_0','PETCT_cdd237e9b3_0','PETCT_ce0ffef966_0','PETCT_93132553f6_0','PETCT_0c13e4df10_0','PETCT_ce629e2993_0','PETCT_d0086487f4_0','PETCT_0e9a98ecda_0','PETCT_515c40c4a6_0','PETCT_960c5f4262_0','PETCT_960c5f4262_1', 'PETCT_5c1baad5d8_0','PETCT_d1f456d229_0', 'PETCT_6c469107a0_0', 'PETCT_59e6d1de22_0','PETCT_d325897ff4_0','PETCT_d325897ff4_1','PETCT_d325897ff4_2','PETCT_11e258cc1f_0','PETCT_9775598501_0','PETCT_d393ab6c7b_0','PETCT_55e3e62722_0','PETCT_13d0984c93_0','PETCT_d46f0109f8_0','PETCT_d472033d3b_0','PETCT_147a9fcff3_0','PETCT_9a2c6e618a_0','PETCT_154e94256c_0','PETCT_9a66a81ad1_0','PETCT_9a66a81ad1_1','PETCT_9a66a81ad1_2','PETCT_9a66a81ad1_3','PETCT_d5e2aa7feb_0','PETCT_9aa97cf103_0','PETCT_16cdbc8689_0','PETCT_9b53627d23_0','PETCT_1774857f8e_0','PETCT_d63f6162a6_0','PETCT_9c36b318e8_0','PETCT_d65cf203be_0','PETCT_d69c3fceba_0','PETCT_185da4c8b6_0','PETCT_d69eabbb20_0','PETCT_d6a48a629d_0','PETCT_d6a48a629d_1','PETCT_345b11778a_0','PETCT_f11f3d3692_0','PETCT_3481507253_0','PETCT_350e91119a_0','PETCT_f1ca0f7c4c_0','PETCT_35de69968e_0','PETCT_dadcd69ba9_0','PETCT_db3daf78d2_0','PETCT_b621742469_0','PETCT_20a607649d_0','PETCT_dd887591a9_0','PETCT_dd975744e7_0','PETCT_2202a936e0_0','PETCT_a61d8768d0_0','PETCT_23ed525e82_0','PETCT_2428b44e92_0','PETCT_a7b323b3fd_0','PETCT_265c26907a_0','PETCT_2716c9bfff_0','PETCT_2716c9bfff_1','PETCT_2716c9bfff_2','PETCT_e344879c2e_0','PETCT_e344879c2e_1','PETCT_275fb00a66_0','PETCT_e4712dc58c_0','PETCT_2791a0b3c2_0','PETCT_29ab45ef17_0','PETCT_2a41141775_0','PETCT_e61c9da258_0','PETCT_e6f6c84ec5_0','PETCT_e77124b7f4_0','PETCT_2ce074c2ea_0','PETCT_2dc17aaeaf_0','PETCT_2e44706eaf_0','PETCT_2f587d00b1_0','PETCT_2f7200f771_0','PETCT_ea6c621616_0','PETCT_ea9302fb0f_0','PETCT_ebaa30ba2e_0','PETCT_302613f9a5_0','PETCT_eca59074b9_0','PETCT_ede28cc3c2_0','PETCT_ef9d41b836_0','PETCT_efd619ecbf_0','PETCT_32aa845af1_0','PETCT_32aa845af1_1','PETCT_335a00191d_0','PETCT_f144b214af_0','PETCT_f1501b1f45_0','PETCT_f15b868db6_0','PETCT_f24f3ce1da_0',
'PETCT_39eca178a1_0','PETCT_f7067b7bbb_0','PETCT_f7a9267a69_0','PETCT_f7a9267a69_1','PETCT_3b2a4af482_0','PETCT_3cf68da275_0','PETCT_faf4a6dbaa_0','PETCT_3f5a9f616f_0','PETCT_fde79b6aa9_0','PETCT_fde79b6aa9_1','PETCT_fde79b6aa9_2','PETCT_411801de5a_0','PETCT_41472f5ce9_0','PETCT_437d2c96fe_0','PETCT_4404466919_0','PETCT_442a09f90e_0','PETCT_8311aeddb9_0','PETCT_8311aeddb9_1','PETCT_824c6a0014_0','PETCT_c227131152_0','PETCT_c16d325d12_0','PETCT_80f21e1ed0_0','PETCT_7fbb39290e_0','PETCT_7faf36a152_0','PETCT_7faf36a152_1','PETCT_bb45bfcffd_0','PETCT_bacc741e2c_0','PETCT_7958ce0f7c_0','PETCT_7948aa0e26_0','PETCT_b62864161e_0','PETCT_77bceab232_0','PETCT_7785c10e91_0','PETCT_777fa0ba88_0','PETCT_777fa0ba88_1','PETCT_76ebd5c736_0','PETCT_760c77b289_0','PETCT_b41bc7c1e5_0','PETCT_b41bc7c1e5_1','PETCT_b41bc7c1e5_2','PETCT_75d5e740f0_0','PETCT_75d1080946_0','PETCT_b2f82ed4b9_0','PETCT_b2f82ed4b9_1','PETCT_741f6130ed_0','PETCT_b2244b5591_0','PETCT_b1de3d4248_0','PETCT_b1d6679284_0','PETCT_7323c415d0_0','PETCT_72d2d6de52_0','PETCT_af73b85f2c_0','PETCT_7147385005_0','PETCT_6fe855c937_0','PETCT_ae6a37a9d6_0','PETCT_ae6a37a9d6_1','PETCT_ae6a37a9d6_2','PETCT_ae6a37a9d6_3','PETCT_ae6a37a9d6_4','PETCT_6e1dba94e8_0','PETCT_6d6a193655_0','PETCT_6d62e15c29_0','PETCT_6d62e15c29_1','PETCT_adc49adb3d_0','PETCT_ad99263bec_0','PETCT_ad7c6a4a58_0','PETCT_ac75e49284_0','PETCT_6b177a3c28_0','PETCT_aaf2c3aa12_0','PETCT_69606f6a25_0','PETCT_68a7ade33c_0','PETCT_65bd1a4c38_0','PETCT_65346b03b8_0','PETCT_642d6c78d6_0','PETCT_642d6c78d6_1','PETCT_63dd9503eb_0','PETCT_63464433c8_0','PETCT_62b114e09b_0','PETCT_62b114e09b_1','PETCT_62405d117c_0','PETCT_61d5bc58fc_0','PETCT_61d5bc58fc_1','PETCT_61d5bc58fc_2','PETCT_61d5bc58fc_3','PETCT_607c1b38e3_0','PETCT_607c1b38e3_1','PETCT_605369e88d_0','PETCT_5e2da717db_0','PETCT_5d10be5b89_0','PETCT_5c57a98a43_0','PETCT_5b10c3f524_0','PETCT_5ac4fd9091_0','PETCT_5951afb86e_0','PETCT_581fa95eb0_0','PETCT_562294be56_0','PETCT_562294be56_1','PETCT_562294be56_2','PETCT_55ae7986e1_0','PETCT_54bed1d98f_0','PETCT_548bd05667_0','PETCT_c2b776974a_0'],


'brain_structure_train': ['dlbs_0028401', 'dlbs_0028402', 'dlbs_0028404', 'dlbs_0028406', 'dlbs_0028407',  'dlbs_0028591','dlbs_0028411', 'dlbs_0028413', 'dlbs_0028415', 'dlbs_0028416', 'dlbs_0028417', 'dlbs_0028418', 'dlbs_0028422', 'dlbs_0028426', 'dlbs_0028427', 'dlbs_0028428', 'dlbs_0028429', 'dlbs_0028430', 'dlbs_0028431', 'dlbs_0028432', 'dlbs_0028436', 'dlbs_0028437', 'dlbs_0028438', 'dlbs_0028440', 'dlbs_0028441', 'dlbs_0028443', 'dlbs_0028445', 'dlbs_0028446', 'dlbs_0028447', 'dlbs_0028450', 'dlbs_0028451', 'dlbs_0028454', 'dlbs_0028455', 'dlbs_0028456', 'dlbs_0028457', 'dlbs_0028458', 'dlbs_0028460', 'dlbs_0028461', 'dlbs_0028462', 'dlbs_0028463', 'dlbs_0028466', 'dlbs_0028467', 'dlbs_0028468', 'dlbs_0028469', 'dlbs_0028470', 'dlbs_0028472', 'dlbs_0028473', 'dlbs_0028474', 'dlbs_0028475', 'dlbs_0028476', 'dlbs_0028477', 'dlbs_0028479', 'dlbs_0028480', 'dlbs_0028481', 'dlbs_0028482', 'dlbs_0028483', 'dlbs_0028486', 'dlbs_0028487', 'dlbs_0028488', 'dlbs_0028491', 'dlbs_0028492', 'dlbs_0028493', 'dlbs_0028494', 'dlbs_0028495', 'dlbs_0028497', 'dlbs_0028499', 'dlbs_0028500', 'dlbs_0028501', 'dlbs_0028503', 'dlbs_0028504', 'dlbs_0028506', 'dlbs_0028507', 'dlbs_0028508', 'dlbs_0028509', 'dlbs_0028510', 'dlbs_0028512', 'dlbs_0028514', 'dlbs_0028515', 'dlbs_0028516', 'dlbs_0028518', 'dlbs_0028519', 'dlbs_0028520', 'dlbs_0028521', 'dlbs_0028522', 'dlbs_0028524', 'dlbs_0028526', 'dlbs_0028527', 'dlbs_0028528', 'dlbs_0028529', 'dlbs_0028530', 'dlbs_0028533', 'dlbs_0028534', 'dlbs_0028535', 'dlbs_0028536', 'dlbs_0028537', 'dlbs_0028540', 'dlbs_0028541', 'dlbs_0028542', 'dlbs_0028543', 'dlbs_0028544', 'dlbs_0028545', 'dlbs_0028547', 'dlbs_0028548', 'dlbs_0028552', 'dlbs_0028553', 'dlbs_0028554', 'dlbs_0028556', 'dlbs_0028559', 'dlbs_0028560', 'dlbs_0028561', 'dlbs_0028563', 'dlbs_0028564', 'dlbs_0028565', 'dlbs_0028566', 'dlbs_0028567', 'dlbs_0028568', 'dlbs_0028569', 'dlbs_0028572', 'dlbs_0028573', 'dlbs_0028574', 'dlbs_0028575', 'dlbs_0028576', 'dlbs_0028577', 'dlbs_0028578'],
'brain_structure_val': ['dlbs_0028394', 'dlbs_0028395', 'dlbs_0028397', 'dlbs_0028398', 'dlbs_0028400'],
'brain_structure_test': ['dlbs_0028581', 'dlbs_0028582', 'dlbs_0028583', 'dlbs_0028584', 'dlbs_0028589', 'dlbs_0028590', 'dlbs_0028410', 'dlbs_0028592', 'dlbs_0028593', 'dlbs_0028594', 'dlbs_0028595', 'dlbs_0028596', 'dlbs_0028597', 'dlbs_0028598', 'dlbs_0028599', 'dlbs_0028600', 'dlbs_0028601', 'dlbs_0028603', 'dlbs_0028605', 'dlbs_0028606', 'dlbs_0028607', 'dlbs_0028608', 'dlbs_0028609', 'dlbs_0028610', 'dlbs_0028611', 'dlbs_0028614', 'dlbs_0028617', 'dlbs_0028618', 'dlbs_0028619', 'dlbs_0028621', 'dlbs_0028623', 'dlbs_0028624', 'dlbs_0028625', 'dlbs_0028626', 'dlbs_0028627', 'dlbs_0028628', 'dlbs_0028629', 'dlbs_0028630', 'dlbs_0028633', 'dlbs_0028634', 'dlbs_0028636', 'dlbs_0028637', 'dlbs_0028640'],

}

# The mapping dict to map origin label index to the new overall label index
dataset_lab_map = { 
    'lits': [0, 1], 
    'kits': [2, 3], 
    'amos_ct': [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    'amos_mr': [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    'bcv': [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'structseg_oar': [32, 33, 34, 35, 36, 37],
    'chaos': [38, 39, 40, 41],
    'structseg_head_oar': [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63],
    'mnm': [64, 65, 66],
    'brain_structure': [67, 68, 69],
    'autopet': [70]
}   

# CT: 0, PET: 1, T1 MRI: 2, T2 MRI: 3, cineMRI: 4
dataset_modality_map = { 
    'lits': 0, 
    'kits': 0, 
    'amos_ct': 0,
    'amos_mr': -1, # unknown MRI sequences, don't compute loss
    'bcv': 0,
    'structseg_oar': 0,
    'chaos_t1_in': 2,
    'chaos_t1_out': 2,
    'chaos_t2': 3,
    'structseg_head_oar': 0,
    'mnm': 4,
    'brain_structure': 2,
    'autopet': 1,
}

# The weight to sample each dataset to balance training. Smaller dataset should have higher weight
dataset_sample_weight = { 
    'bcv': 1.5,
    'structseg_oar': 0.7,
    'lits': 0.3,
    'kits': 0.3,
    'amos_ct': 1.8,                                                                                                                        
    'amos_mr': 1.6, 
    'chaos': 0.5, 
    'structseg_head_oar': 2.6,
    'mnm': 0.3, 
    'brain_structure': 0.4, 
    'autopet':  0.1, 
}   

# The parameters for color augmentation, CT and PET images 0.1 while MR images 0.2
dataset_aug_prob = { 
    'bcv': 0.1, 
    'structseg_oar': 0.1, 
    'lits': 0.1, 
    'kits': 0.1, 
    'amos_ct': 0.1,                                                                                                                         
    'amos_mr': 0.2, 
    'chaos': 0.2,
    'structseg_head_oar': 0.1, 
    'mnm': 0.2,
    'brain_structure': 0.1, 
    'autopet':  0.1,  
}   
