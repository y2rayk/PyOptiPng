/*
 * optipng.h
 * OptiPNG programming interface.
 *
 * Copyright (C) 2001-2010 Cosmin Truta.
 *
 * This software is distributed under the zlib license.
 * Please see the attached LICENSE for more information.
 */


#ifndef OPTIPNG_H
#define OPTIPNG_H

#include <stdarg.h>
#include "cbitset.h"


#ifdef __cplusplus
extern "C" {
#endif


/*
 * User options (e.g. extracted from the command line)
 */
struct opng_options
{
#ifndef PYEXT_BUILD
	int help;
#endif
	int fix;
	int force;
	int full;
	int interlace;
	int keep;
	int nb, nc, np, nz;
	int preserve;
#ifndef PYEXT_BUILD
	int quiet;
#endif
	int simulate;
	int snip;
	int verbose;
#ifndef PYEXT_BUILD
	int version;
#endif
	int optim_level;
	bitset_t compr_level_set;
	bitset_t mem_level_set;
	bitset_t strategy_set;
	bitset_t filter_set;
	int window_bits;
	char *out_name;
	char *dir_name;
#ifndef PYEXT_BUILD
	char *log_name;
#endif
};

/*
 * User interface callbacks
 */
struct opng_ui
{
	void (*printf_fn)(const char *fmt, ...);
	void (*print_cntrl_fn)(int cntrl_code);
	void (*progress_fn)(unsigned long current_step, unsigned long total_steps);
	void (*panic_fn)(const char *msg);
};


/*
 * Engine initialization
 */
int opng_initialize(const struct opng_options *options,
					const struct opng_ui *ui);


/*
 * Engine execution
 */
int opng_optimize(const char *infile_name);


/*
 * Engine finalization
 */
int opng_finalize(void);


/*
 * Encoder limits and default values
 */
#define OPNG_OPTIM_LEVEL_DEFAULT    2
#define OPNG_OPTIM_LEVEL_MIN        0
#define OPNG_OPTIM_LEVEL_MAX        7

#define OPNG_COMPR_LEVEL_MIN        1
#define OPNG_COMPR_LEVEL_MAX        9
#define OPNG_COMPR_LEVEL_SET_MASK   ((1 << (9+1)) - (1 << 1))  /* 0x03fe */

#define OPNG_MEM_LEVEL_MIN          1
#define OPNG_MEM_LEVEL_MAX          9
#define OPNG_MEM_LEVEL_SET_MASK     ((1 << (9+1)) - (1 << 1))  /* 0x03fe */

#define OPNG_STRATEGY_MIN           0
#define OPNG_STRATEGY_MAX           3
#define OPNG_STRATEGY_SET_MASK      ((1 << (3+1)) - (1 << 0))  /* 0x000f */

#define OPNG_FILTER_MIN             0
#define OPNG_FILTER_MAX             5
#define OPNG_FILTER_SET_MASK        ((1 << (5+1)) - (1 << 0))  /* 0x003f */


#ifdef __cplusplus
}  /* extern "C" */
#endif


#endif  /* OPTIPNG_H */
